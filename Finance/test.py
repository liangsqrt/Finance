#_*_coding:utf-8_*_
from lxml import etree
from scrapy import Selector

this_div='''

<div id="zwlist">
                
                <div class="zwli clearfix" id="zwli8494972927" data-huifuid="8494972927" data-huifuuid="7661094278080258">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8494972927">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/7661094278080258"><img src="http://avator.eastmoney.com/qface/7661094278080258/30" data-popper="7661094278080258" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/7661094278080258"  data-popper="7661094278080258" data-poptype="1">屋脊飞</a></span> <span class="influence" data-uid="7661094278080258"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-06  05:05:57</div>

                            
                            <div class="zwlitext stockcodec">对股市懂得挺多的人，越不轻易对市场行情发表意见。 </div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>

'''

# datalxml=etree.HTML(this_div)
# print datalxml.xpath('//div[@id="zwlist"]//div[@class="zwlitext stockcodec"]/@class')[0]

sel=Selector(text=this_div,type='html')

print sel.xpath('//div[@id="zwlist"]//div[@class="zwlitext stockcodec"]/').extract()