import xarray as xr
import pandas as pd
from sklearn.decomposition import PCA

class FeatureExtractor():
    def __init__(self):
        self.means = {}
        self.sds = {}
        self.variables = ["TS", "PSL", "TMQ"]
        self.pca = {}
        self.num_comps = 20

    def fit(self, X_ds, y):
        for var in self.variables:
            if var not in self.means.keys():
                self.means[var] = X_ds[var].mean(axis=0).values
                self.sds[var] = X_ds[var].std(axis=0).values
                self.sds[var][self.sds[var] == 0] = 1
            var_norm = (X_ds[var] - self.means[var]) / self.sds[var]
            var_flat = var_norm.stack(latlon=("lat", "lon")).values
            var_flat[np.isnan(var_flat)] = 0
            self.pca[var] = PCA(n_components=self.num_comps)
            self.pca[var].fit(var_flat)


    def transform(self, X_ds):
        X = np.zeros((np.prod(X_ds[self.variables[0]].shape[:1]), 
                      self.num_comps * len(self.variables)), dtype=np.float32)
        c = 0
        for var in self.variables:
            var_norm = (X_ds[var] - self.means[var]) / self.sds[var]
            var_flat = var_norm.stack(latlon=("lat", "lon")).values
            var_flat[np.isnan(var_flat)] = 0
            X[:, c:c+self.num_comps] = self.pca[var].transform(var_flat)
            c += self.num_comps
        return X
