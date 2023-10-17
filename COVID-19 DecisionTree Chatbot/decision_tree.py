import numpy as np

class Decision_Tree:
    def __init__(self,data,label) -> None:
        self.data = data
        self.labels = label
        entropy_label = self.entropy(data[label])

        for feature in data.columns[:-1]:
            entropy_feature =0
            for value in data[feature].unique():
                subset = data[data[feature]==value]
                proportion  = len(subset)/len(data)
                entropy_feature += proportion * self.entropy(subset[label])

            info_gain = self.information_gain(data,feature,label)

    
    def entropy(self,labels):
        _,counts = np.unique(labels,return_counts=True)
        probs = counts/len(labels)
        return -np.sum(probs*np.log2(probs))


    def information_gain(self,data,feature,label):
        feature_entropy = 0
        for value in data[feature].unique():
            subset=data[data[feature]==value]
            proprtion = len(subset)/ len(data)
            feature_entropy += proprtion * self.entropy(subset[label])

        return self.entropy(data[label]) - feature_entropy
    
    def _build_tree(self,data,label,parent=None,edge_label=None):
        if len(data[label].unique()) ==1:
            value = data[label].unique()[0]
            return str(value)
        elif len(data.columns) == 1:
            value = data[label].value_counts().idxmax()
            return str(value)
        else:
            best_feature  = max(data.columns[:-1],key= lambda feature:self.information_gain(data,feature,label))
            tree = {best_feature:{}}
            for value in data[best_feature].unique():
                subset = data[data[best_feature]==value]
                tree[best_feature][value] = self._build_tree(subset.drop(best_feature,axis=1),label,best_feature,value)

            return tree
        
    

        
    def build_tree(self):
        return self._build_tree(self.data,self.labels)