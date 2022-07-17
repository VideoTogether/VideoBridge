# VideoBridge
Modified video player scripts

This project is a bridge connecting the video player to VideoTogether extension.

一些视频网站使用 wasm 解码器，导致脚本很难控制这些播放器。这里我们用一种取巧的方式，通过修改这些播放器的脚本，将可操作的player对象暴露出来，从而使 VideoTogether 能够控制这些播放器。

这些网站的播放器脚本地址可能会更新，欢迎提交 player_list.json 的 PR