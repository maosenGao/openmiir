![OpenMIIR: a public domain dataset of EEG recordings for music imagery information retrieval](https://raw.githubusercontent.com/sstober/openmiir/master/logo/OpenMIIR-logo_transparent_728x265.png)

Music imagery information retrieval (MIIR) systems may one day be able to recognize a song just as we think of it.
音乐意象信息恢复(MIIR)系统也许有一天能够识别出我们所认为的歌曲。

As a step towards such technology, we are presenting a public domain dataset of electroencephalography (EEG) recordings taken during music perception and imagination.
作为向这一技术迈进的一步，我们展示了一个公共领域的脑电图(EEG)数据集，它记录了音乐感知和想象过程。
我们是在一项正在进行的研究中获得这些数据的。

We acquired this data during an ongoing study that so far comprised 10 subjects listening to and imagining 12 short music fragments - each 7s-16s long - taken from well-known pieces. 
到目前为止，这项研究包括10名受试者，他们分别听和想象12段短的音乐片段——每段都有7 -16秒长——这些片段都是从著名的音乐片段中截取的。

These stimuli were selected from different genres and systematically span several musical dimensions such as meter, tempo and the presence of lyrics.
This way, various retrieval and classification scenarios can be addressed.
这些刺激来自不同的体裁，系统地跨越了几个音乐维度，如节奏、节奏和歌词的存在。
通过这种方式，可以解决各种检索和分类场景。

The dataset is primarily aimed to enable music information retrieval researchers interested in these new MIIR challenges to easily test and adapt their existing approaches for music analysis like fingerprinting, beat tracking or tempo estimation on this new kind of data.
该数据集的主要目的是使对这些新的MIIR挑战感兴趣的音乐信息检索研究人员能够容易地测试和调整他们现有的音乐分析方法，如指纹、节拍跟踪或节拍估计等这种新的数据。

We also hope that the OpenMIIR dataset will facilitate a stronger interdisciplinary collaboration between music information retrieval researchers and neuroscientists.
我们也希望OpenMIIR数据集能够促进音乐信息检索研究者和神经科学家之间更强的跨学科合作




## Obtaining the Raw EEG Data

This git repository does not contain the raw EEG data, which is around 700 MB per subject adding up to several gigabytes in total. There are currently two ways to obtain the data:

这个git存储库不包含原始的EEG数据，每个受试者大约有700mb的数据，总计达几个gb。原始的eeg信号目前获取数据有两种方式:

1. download via http from one of the sites listed below:
	- [University of Potsdam](http://www.ling.uni-potsdam.de/mlcog/OpenMIIR-RawEEG_v1/)
	- [University of Western Ontario](<http://bmi.ssc.uwo.ca/OpenMIIR-RawEEG_v1/>)

2. download via bittorrent tracked by [academic torrents](<http://academictorrents.com/details/c18c04a9f18ff7d133421012978c4a92f57f6b9c>)

We strongly encorage the second approach as it allows for distributed sharing.


## Data Processing

In order to enable everybody to work with this data, we decided to share it in a format that does not require any commercial software for loading and processing. Specifically, the raw EEG is saved in the FIF file format used by [MNE](<http://martinos.org/mne/>) and [MNE-Python](<http://martinos.org/mne/stable/mne-python.html>). 

为了使每个人都能处理这些数据，我们决定以一种不需要任何商业软件来加载和处理的格式来共享这些数据。
具体来说，原始的EEG以“MNE1(<http://martinos.org/mne/>)和[MNE-Pythonl(< http://martinos.org/mne/stable /mne-python.html)”所使用的FIF文件格式保存。

This data format can, for instance, also be easily converted into the MAT format used by Matlab, which allows importing into EEGLab. A description on how to do this can be found [in the wiki](<https://github.com/sstober/openmiir/wiki/How-to-import-the-raw-EEG-data-into-EEGLab>).
例如，这种数据格式也可以很容易地转换成Matlab使用的MAT格式，这样就可以将其导入EEGLab。
在wikil(chttps:// github.com/sstober/openmiir/wiki/howto -import-the- raw-egle -data-into- eeglab >)中可以找到如何做到这一点的描述。

For further processing, we provide custom dataset implementations and deep learning pipelines for [pylearn2](<https://github.com/lisa-lab/pylearn2>) within the [deepthought](<https://github.com/sstober/deepthought>) project. 

为了进一步处理，我们提供了自定义数据集实现和深度学习管道
[pylearn2](chttps://github.com/lisa-lab/pvlearn2>)在[deepthougus deepthought tl(<https://github.com/sstober/ deepthought>)项目中。

## More Information

A first presentation about this dataset was given at [NEMISIG 2015](<http://jimi.ithaca.edu/nemisig/>) and can be downloaded [here](<http://bib.sebastianstober.de/2015-01-31_NEMISIG.pdf>).
关于这个数据集的第一次展示是在“NEMISIG 28151”(<http://iimi.ithaca。可下载[herel (chttp://bib]。sebastianstober。

Furthermore, there is information about [labs using this dataset](<https://github.com/sstober/openmiir/wiki/Labs-using-this-Dataset>) and [related publications](<https://github.com/sstober/openmiir/wiki/Related-Publications>) in the [repository wiki](<https://github.com/sstober/openmiir/wiki>). Please contact us, if you would like to be added.

此外，在“知识库wikil”(< https://github.com/sstober/openmiir/wiki/openmiir/openmiir/openmiir/openmiir/wiki/relatpublications >)中有关于“使用该数据集的实验室”(< https://github.com/sstober/openmiir/openmiir/openmiir/wiki/openmiir/openmiir/wiki >)的信息。
请联系我们，如果你想增加。

## Contributing

You are openly invited to contribute to this dataset. There are several possibilities to do this:

- add more subjects by running the experiment yourself
- host an http download mirror or seed the dataset torrent to provide download bandwidth
- run your own experiments on the dataset and share your results
- ...

If you want to contribute, please contact us.
您被公开邀请为这个数据集做贡献。
有几种可能做到这一点:
	通过自己运行实验来添加更多的主题
	托管一个http下载镜像或种子数据集种子以提供下载带宽。
	在数据集上运行您自己的实验并共享vour
	结果如果你想投稿，请联系我们。

## License and Citations

OpenMIIR is released under the [Open Data Commons Public Domain Dedication and Licence (PDDL)](<http://opendatacommons.org/licenses/pddl/1-0/>), which means that you can freely use it without any restrictions.

If you use the OpenMIIR dataset in published research work, we would appreciate if you would cite this article: 
Sebastian Stober, Avital Sternin, Adrian M. Owen and Jessica A. Grahn: **"Towards Music Imagery Information Retrieval: Introducing the OpenMIIR Dataset of EEG Recordings from Music Perception and Imagination."** In: Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR’15), pages 763-769, 2015. 
OpenMIIR是在[Open Data Commons Public Domain Dedication and Licence (PDDL)](<http://opendatacommons.org/ licenses/pdd1/1-8/>)下发布的，这意味着您可以不受任何限制地自由使用它。
如果您在已发表的研究工作中使用OpenMIIR数据集，我们希望您能引用这篇文章:Sebastian Stober, Avital Sternin, Adrian M. Owen和Jessica A. Grahn: **“音乐图像信息检索:介绍了OpenMIIR的音乐感知和想象脑电图记录数据集。“** In: 16日议程国际音乐信息检索学会会议(ISMIR'15)，第763-769页，2815页。

## Acknowledgments

This dataset is a result of ongoing joint work between the [Owen Lab](<http://www.owenlab.uwo.ca/>) and the [Music and Neuroscience Lab](<http://www.jessicagrahn.com/>) at the [Brain and Mind Institute](<http://www.uwo.ca/bmi/>) of the [University of Western Ontario](<http://www.uwo.ca/>).
It has been supported by a fellowship within the Postdoc-Program of the German Academic Exchange Service (DAAD), the Canada Excellence Research Chairs (CERC) Program, an National Sciences and Engineering Research Council (NSERC) Discovery Grant and an Ontario Early Researcher Award.
该数据集是fowen实验室正在进行的联合工作的结果[chttp://www.owenlab]。uwo.ca/>)和音乐与神经科学实验室(<http://www.iessicagrahn.com/>)。Uwo。
加拿大安大略省西部rUniversity (chttp://ww)的ca/bmi/>。Uwo.ca / >)它获得了德国学术交流服务(DAAD)博士后项目、加拿大卓越研究委员会(CERC)项目、国家科学与工程研究委员会的奖学金支持。(NSERC)发现奖和安大略省早期研究员奖。

## Contact

Sebastian Stober \<sstober AT uni-potsdam DOT de\>  
Machine Learning in Cognitive Science Lab  
Research Focus Cognitive Sciences  
University of Potsdam, Germany  

德国波茨坦大学的Sebastian Stober <sstober >300er机器学习在认知科学实验室的研究重点是认知科学大学波茨坦，德国


[http://www.owenlab.uwo.ca/](<http://www.owenlab.uwo.ca/>)  
[http://www.jessicagrahn.com/](<http://www.jessicagrahn.com/>)  
[http://www.uni-potsdam.de/mlcog/](<http://www.uni-potsdam.de/mlcog/>)  