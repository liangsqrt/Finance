from bs4 import BeautifulSoup

this_div='''

<div class="zwli clearfix" id="zwli8503741597" data-huifuid="8503741597" data-huifuuid="6636013731571078">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8503741597">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6636013731571078"><img src="http://avator.eastmoney.com/qface/6636013731571078/30" data-popper="6636013731571078"></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6636013731571078" data-popper="6636013731571078" data-poptype="1">beidouxing5000</a></span> <span class="influence" data-uid="6636013731571078"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-20  22:08:05</div>

                            
                            <div class="zwlitext stockcodec"><img src="http://gbres.dfcfw.com/face/emot/emot19.png" title="赞"></div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>

'''


datasoup=BeautifulSoup(this_div,'lxml')
print datasoup.select('.zwlitext.stockcodec')[0]