'''
Created by auto_sdk on 2020.05.19
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceProjectQueryRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.project.query'
