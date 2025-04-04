import os

import anndata
import pytest

import scvi

from .utils import unsupervised_training_one_epoch


@pytest.mark.internet
def test_pbmc_dataset(save_path: str):
    dataset = scvi.data.pbmc_dataset(
        save_path=save_path,
        remove_extracted_data=True,
    )
    unsupervised_training_one_epoch(dataset)


@pytest.mark.internet
def test_retina_dataset(save_path: str):
    dataset = scvi.data.retina(save_path=save_path)
    unsupervised_training_one_epoch(dataset, batch_key="batch")


@pytest.mark.internet
def test_pfc_starmap_dataset(save_path: str):
    gene_dataset = scvi.data.prefrontalcortex_starmap(save_path=save_path)
    unsupervised_training_one_epoch(gene_dataset)


@pytest.mark.internet
@pytest.mark.parametrize("name", ["1", "2", "3"])
def test_annotated_dataset(name: str, save_path: str):
    dataset = scvi.data.annotation_simulation(name=name, save_path=save_path)
    unsupervised_training_one_epoch(dataset)


@pytest.mark.internet
def test_fc_dropseq_dataset(save_path: str):
    gene_dataset = scvi.data.frontalcortex_dropseq(save_path=save_path)
    unsupervised_training_one_epoch(gene_dataset)


@pytest.mark.internet
@pytest.mark.parametrize("high_level_cluster", [True, False])
def test_smfish_dataset(high_level_cluster: bool, save_path: str):
    gene_dataset = scvi.data.smfish(use_high_level_cluster=high_level_cluster, save_path=save_path)
    unsupervised_training_one_epoch(gene_dataset)


@pytest.mark.internet
def test_cortex_dataset(save_path: str):
    adata = scvi.data.cortex(save_path=save_path)
    unsupervised_training_one_epoch(adata, labels_key="cell_type")


@pytest.mark.internet
def test_brainlarge_dataset(save_path: str):
    adata = scvi.data.brainlarge_dataset(
        save_path=save_path,
        sample_size_gene_var=10,
        n_genes_to_keep=10,
        max_cells_to_keep=128,
    )
    unsupervised_training_one_epoch(
        adata,
    )


@pytest.mark.internet
def test_breast_cancer_dataset(save_path: str):
    adata = scvi.data.breast_cancer_dataset(
        save_path=save_path,
    )
    unsupervised_training_one_epoch(
        adata,
    )


@pytest.mark.internet
def test_mouse_ob_dataset(save_path: str):
    adata = scvi.data.mouse_ob_dataset(
        save_path=save_path,
    )
    unsupervised_training_one_epoch(
        adata,
    )


@pytest.mark.internet
def test_download_spleen_lymph_data(save_path: str):
    scvi.data.spleen_lymph_cite_seq(save_path=save_path)
    scvi.data.spleen_lymph_cite_seq(save_path=save_path, protein_join="outer")


@pytest.mark.internet
def test_download_heart_cell_atlas(save_path: str):
    scvi.data.heart_cell_atlas_subsampled(save_path=save_path)


@pytest.mark.internet
def test_download_seurat_v4_pbmc(save_path: str):
    scvi.data.pbmc_seurat_v4_cite_seq(save_path=save_path, mask_protein_batches=5)


@pytest.mark.internet
def test_download_cellxgene(save_path: str):
    url = "https://cellxgene.cziscience.com/e/de985818-285f-4f59-9dbd-d74968fddba3.cxg/"
    filename = "cellxgene.h5ad"
    scvi.data.cellxgene(url, save_path=save_path, filename=filename)
    anndata.read_h5ad(os.path.join(save_path, filename))
