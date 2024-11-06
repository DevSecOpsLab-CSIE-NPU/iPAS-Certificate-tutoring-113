# 安裝 Jupyter Notebook

## 1. Install Miniconda 安裝 Miniconda

1. Go to [this link](https://docs.anaconda.com/miniconda/) and download Miniconda. 前往[這個連結](https://docs.anaconda.com/miniconda/)並下載 Miniconda。
2. Install Miniconda. 安裝 Miniconda。
3. Check your environment. 檢查你的環境。

## 2. Clone the Repository 複製儲存庫

Run the following command to clone the repository: 執行以下命令來複製儲存庫：

```bash=
git clone https://github.com/DevSecOpsLab-CSIE-NPU/iPAS-Certificate-tutoring-113
```

## 3. Install [Jupyter Notebook](https://jupyter.org/install#jupyter-notebook) 安裝 [Jupyter Notebook](https://jupyter.org/install#jupyter-notebook)

1. Change directory to your cloned folder, e.g., `cd iPAS-Certificate-tutoring-113/`. 切換目錄到你複製的資料夾，例如 `cd iPAS-Certificate-tutoring-113/`。
2. Create a virtual environment with `python3 -m venv .venv`. On Windows, use `.\.venv\Scripts\activate`. 使用 `python3 -m venv .venv` 創建虛擬環境。在 Windows 上，使用 `.\.venv\Scripts\activate`。
3. Install Jupyter Notebook by running `ipython -m pip install notebook`. 執行 `ipython -m pip install notebook` 安裝 Jupyter Notebook。
4. Open `Your_code_here/hello.ipynb` and start coding. 打開 `Your_code_here/hello.ipynb` 並開始編碼。

## 4. Install Plugin [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 安裝外掛 [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

```text
Name: Jupyter
Id: ms-toolsai.jupyter
Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more. 
Version: 2024.10.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
```

And check out how to use it at https://code.visualstudio.com/docs/datascience/jupyter-notebooks. 並查看如何使用 https://code.visualstudio.com/docs/datascience/jupyter-notebooks。

## 5. 在 Visual Studio Code 裡，打開練習程式

Open [hello.iynb](113_fall/Your_code_here/hello.ipynb)