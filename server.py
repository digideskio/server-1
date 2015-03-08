import cherrypy
import cherrypy_cors

class Server(object):
	@cherrypy.expose
	def index(self):
		return "HELLO WORLD!"

	@cherrypy.expose
	#@cherrypy_cors.tools.expose()
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in(force=False)
	def query(self, curr_lat=0, curr_lng=0, dest_lat=0, dest_lng=0):
		ret = {
			'coords': None,
		}

		# DO PATH COORDINATES FINDING STUFF HERE

		ret['coords'] = "returned: " + curr_lat + curr_lng + dest_lat + dest_lng
		return ret

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	cherrypy.config.update({'tools.CORS.on': True,})
	cherrypy.server.socket_host = '0.0.0.0'
	cherrypy.quickstart(Server())
