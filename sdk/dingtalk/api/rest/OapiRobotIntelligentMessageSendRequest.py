'''
Created by auto_sdk on 2020.07.03
'''
from dingtalk.api.base import RestApi
class OapiRobotIntelligentMessageSendRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.msg_key = None
		self.msg_param = None
		self.open_conversation_id = None
		self.receiver_union_ids = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.robot.intelligent.message.send'
