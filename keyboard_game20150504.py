import wx
import random
key_down_count = 0
right_count = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'
class Game_GUI(wx.Frame):
	"""docstring for Game_GUI"""
	def __init__(self, *args, **kws):
		super(Game_GUI, self).__init__(*args, **kws)

		self.InitUI()
		self.SetSize((400,200))
		self.Centre()
		self.Show()
	
	def InitUI(self):
		panel = wx.Panel(self)
		self.CreateStatusBar()
		self.characters = wx.StaticText(self, label='',pos=(200,50),size=(100,100))
		self.char = alpha[random.randint(0,25)]
		self.characters.SetLabel(self.char)
		panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		panel.SetFocus()

		

	def OnKeyDown(self,e):
		global key_down_count
		global right_count
		key = e.GetKeyCode()
		key_down_count += 1

		if (key+32) == ord(self.char):
			right_count += 1
			self.char = alpha[random.randint(0,25)]
			self.characters.SetLabel(self.char)
		#在底栏显示正确率
		sb = self.GetStatusBar()
		msg = str(right_count)+'/'+str(key_down_count)
		sb.SetStatusText(msg)
		



if __name__ == '__main__':
	ex = wx.App()
	zero = Game_GUI(None)
	ex.MainLoop()
