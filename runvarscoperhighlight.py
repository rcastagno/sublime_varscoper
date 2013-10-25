import sublime, sublime_plugin
import urllib
from xml.dom import minidom

class runvarscoperhighlighCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		varscoper_cfm_url = self.view.settings().get('varscoper_cfm_url', 'http://localhost/tools/varscoper/varScoper.cfm')

		varScoperBaseURL = varscoper_cfm_url+'?displayFormat=xml&'
		if len(self.view.file_name()) > 0:
			varScoperLink = varScoperBaseURL + 'filePath=' + self.view.file_name()
			print(varScoperLink)
			try:
				proxy_support = urllib.request.ProxyHandler({})
				opener = urllib.request.build_opener(proxy_support)
				urllib.request.install_opener(opener)
				http_handler = urllib.request.HTTPHandler()
				opener = urllib.request.build_opener(http_handler)
				req = urllib.request.Request(varScoperLink)
				resp = urllib.request.urlopen(req)

				code = urllib.request.urlopen(varscoper_cfm_url).getcode()
				if code != 200:
					sublime.error_message('Server '+varscoper_cfm_url+' non raggiungibile')
					return

				data = resp.read()
				print(data)

				xmldoc = minidom.parseString(data)
				itemlist = xmldoc.getElementsByTagName('line_number') 
				first = False
				regions = []
				for s in itemlist :
					line = self.getText(s.childNodes)
					print(line)
					p = self.view.text_point(int(line)-1, 0)
					regions.append(self.view.full_line(p))

				self.view.add_regions('varscoper', regions, 'string', 'cross')
				
				if len(regions) > 0:
					if(not first):
						self.view.show(p)
						first = True

				if len(itemlist) > 0:
					sublime.error_message("Found " + str(len(itemlist)) + " VarScoper violations")

			except (urllib.error.HTTPError) as e:
				sublime.error_message(str(e))

	def getText(self, nodelist):
		rc = []
		for node in nodelist:
			if node.nodeType == node.TEXT_NODE:
				rc.append(node.data)
		return ''.join(rc)