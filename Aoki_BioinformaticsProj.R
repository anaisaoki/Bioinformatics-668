
library(Seurat)
#Reading in the expression matrix
exp.mat <- read.table(file = "/nestorawa_forcellcycle_expressionMatrix.txt", header = TRUE,
                      as.is = TRUE, row.names = 1)
View(exp.mat)

s.genes <- cc.genes$s.genes
g2m.genes <- cc.genes$g2m.genes

#creating the Seurat object and completing initializing steps
marrow <- CreateSeuratObject(counts = exp.mat)
marrow <- NormalizeData(marrow) #log-normalization
marrow <- FindVariableFeatures(marrow, selection.method = "vst") #finding gene variances
marrow <- ScaleData(marrow, features = rownames(marrow)) #centering & scaling data

#Regress signal in variance that cannot be explained by lineage
#For this example, PC8 and PC10 are split on cell cycle genes TOP2A & MK167
marrow <- RunPCA(marrow, features = VariableFeatures(marrow), ndims.print = 6:10, nfeatures.print = 10)
DimHeatmap(marrow, dims = c(8, 10))

#Assigning each cell a score based on its expression
marrow <- CellCycleScoring(marrow, s.features = s.genes, g2m.features = g2m.genes, set.ident = TRUE)
# view cell cycle scores and phase assignments
head(marrow[[]])

# Visualize the distribution of cell cycle markers across
RidgePlot(marrow, features = c("PCNA", "TOP2A", "MCM6", "MKI67"), ncol = 2)

# Running a PCA on cell cycle genes reveals, unsurprisingly, that cells separate entirely by phase
marrow <- RunPCA(marrow, features = c(s.genes, g2m.genes))
DimPlot(marrow)

#Regressing out cell cycle scores during data scaling: this steps takes a while
marrow <- ScaleData(marrow, vars.to.regress = c("S.Score", "G2M.Score"), features = rownames(marrow))
# Now, a PCA on the variable genes no longer returns components associated with cell cycle
marrow <- RunPCA(marrow, features = VariableFeatures(marrow), nfeatures.print = 10)
# When running a PCA on only cell cycle genes, cells no longer separate by cell-cycle phase
marrow <- RunPCA(marrow, features = c(s.genes, g2m.genes))
DimPlot(marrow)

#Alternate workflow
marrow$CC.Difference <- marrow$S.Score - marrow$G2M.Score
#This step takes a five or so minutes complete 
marrow <- ScaleData(marrow, vars.to.regress = "CC.Difference", features = rownames(marrow))
# cell cycle effects strongly mitigated in PCA
marrow <- RunPCA(marrow, features = VariableFeatures(marrow), nfeatures.print = 10)
# when running a PCA on cell cycle genes, actively proliferating cells remain distinct from G1
# cells however, within actively proliferating cells, G2M and S phase cells group together
marrow <- RunPCA(marrow, features = c(s.genes, g2m.genes))
DimPlot(marrow)
