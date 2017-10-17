import requests
from bs4 import BeautifulSoup
import pymongo
from bson.code import Code

client=pymongo.MongoClient('localhost',27017)
COL=client['Finance']
DOC=COL['DFCFW10_4']


mapfunction=Code('''
function(){
	
	var publish_user_list=new Array();
	
	publish_user_href=this.publish_user_href;
	emit('publish_user',publish_user_href);

}
'''
                 )
reducefunction=Code('''
function(key,values){
	return {
		key:values
	};
}
''')

result=DOC.map_reduce(map=mapfunction,reduce=reducefunction,out='myresults')
print result