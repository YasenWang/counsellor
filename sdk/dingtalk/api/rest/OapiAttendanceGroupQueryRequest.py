'''
Created by auto_sdk on 2020.03.31
'''
from dingtalk.api.base import RestApi
class OapiAttendanceGroupQueryRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.group_id = None
		self.op_user_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.group.query'
