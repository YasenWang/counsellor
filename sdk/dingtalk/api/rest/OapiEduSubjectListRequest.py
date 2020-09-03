'''
Created by auto_sdk on 2020.08.11
'''
from dingtalk.api.base import RestApi
class OapiEduSubjectListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.codes = None
		self.cursor = None
		self.data_order_type = None
		self.operator_userid = None
		self.size = None
		self.sort_type = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.subject.list'
