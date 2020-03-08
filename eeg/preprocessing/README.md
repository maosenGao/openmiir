This directory contains information about import and preprocessing of the raw EEG.

这个目录包含关于原始脑电图的导入和预处理的信息。


* notebooks - one jupyter notebook per subject with all steps of the common preprocessing pipeline. 

Except for the initial conversion from raw Biosemi format and basic event processing, all steps can be customized.


笔记本-每名受试者一个木星笔记本，包含通用预处理管道的所有步骤。


除了原始Biosemi格式的初始转换和基本事件处理之外，所有步骤都可以定制



* ica - per-subject ICA parameters for eye blink removal. 
ica -每个受试者的ica参数，用于去除眨眼。
ICA is computed during preprocessing and components that correlate with eye blinks are zeroed out.
ICA在预处理过程中计算，与eve blinks相关的组件被归零。
 But the transformation is not applied to the raw data at that point. I.e., 
但是此时转换并不应用于原始数据。
the raw data remains unchanged and the transformation can be optionally applied after loading a file using the ICA file 
without having to go through the expensive ICA computation again.
即。，原始数据保持不变，可以选择在使用ICA文件加载文件后应用转换，而不必再次执行昂贵的ICA计算。
