# 你的第二个项目：剪刀石头布
## 项目概述 

这是你的第二个项目，你将要在这个项目中实现一个 互动游戏：剪刀石头布 。

在这个项目中，你需要使用到课程中教授的string函数类，random函数 及 控制流。


## 项目指南

### 步骤

1. 克隆存储库并打开下载的文件夹。

 ```	
https://github.com/CheneyZeng/kivy_game.git
```

2. 安装必要的 Python 依赖包 （参见你的第一个项目）


	对于 __Mac/OSX__：
	
	```bash
	conda env create -n my_python
	source activate my_python
	conda install ipykernel
	pip install -r require.txt
	python -m ipykernel install --user --name my_python --display-name "Python:my_python"
	```

	对于 __Windows__：
	
	```bash
	conda create --name my_python python=3.6
	activate my_python
	conda install ipykernel
	pip install -r require_windows.txt
	python -m ipykernel install --user --name my_python
	```
	
3. 打开 notebook

```
jupyter notebook
```

4. 改变环境

[image1]: changekernel.png "Sample Output"

如图![Sample Output][image1]来kernel改成 **Python:my_python**。


__注意：__ 我们虽然已经实现了一些代码，让你更快地开始工作，你仍需要实现额外的功能，以回答 notebook 中所有的问题。
__除非有要求，否则不要修改任何已经包含的代码。__

## 项目评审

你的项目将会由优达学城的审阅者依据次项目的[评审标准](https://review.udacity.com/#!/rubrics/2463/view)进行审阅。请仔细阅读，并在提交之前自我评估你的项目。你必须通过了规则中的所有要求，才会审核通过。

## 项目提交

当你准备好提交你的项目时，将下列文件整理并压缩成一个文件，以便上传。

- 代码完整可运行的文件 `Game wiz Computer.ipynb`，所有的代码块都要执行并展示结果，并要求回答所有问题
- 将你的 notebook 导出为 HTML 以及 py 格式，并以 `Game wiz Computer.html` 以及 `Game wiz Computer.py` 命名
- 任何用于项目中，并且并非由我们为这一项目提供的额外数据图片。
