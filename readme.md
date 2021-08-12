# FF
<!-- ![](https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg "credit to Nick Shillingford")   -->
<!-- <center><img src="https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg" ...></center> -->

FF is a python environment which offers a REPL for audio playback using FFMPEG's FFPlay. Because of this leverage, it is capable of decoding all common audio formats, letting you catchup on all your podcasts from the comfort of your terminal.  
You can customize it to fit your system/workflow by editing the [env](./cns/env.py) file.  

**why?** because you're worth it. But also, I don't have internet regular access from my main station so I tend to use offline media. I also have trouble with heat causing "meltdowns" of my computer (big up HP for putting out "beats" laptops which can't handle even modest DSP tasks), so having something light weight to play back audio is quite essential for me.  
[**how**](#usage)?  

### Usage  

##### Start
This starts the REPL which *-imports all of the contents from the [env](./ff/env.py) file.  
```shell
$ ff
```

##### Control
```python
>>> ff()
# play the file whose path is on your clipboard
>>> rm()
# delete the file whose path is on your clipboard
```



<!-- 
### Change Log
**v 1.0.1**
 -->
