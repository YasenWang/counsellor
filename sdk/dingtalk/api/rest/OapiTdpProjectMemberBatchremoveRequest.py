'''
Created by auto_sdk on 2020.03.31
'''
from dingtalk.api.base import RestApi
class OapiTdpProjectMemberBatchremoveRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.microapp_agent_id = None
		self.operator_userid = None
		self.project_id = None
		self.userids = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.tdp.project.member.batchremove'
