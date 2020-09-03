'''
Created by auto_sdk on 2020.08.05
'''
from dingtalk.api.base import RestApi
class OapiEduSubjectUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.code = None
		self.name = None
		self.operator_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.subject.update'
