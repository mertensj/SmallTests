#!/usr/bin/python2
import gtk
import pygtk
# 
#
def hello(data=None):
	print "Hello ..."

def destroy(data=None):
	gtk.main_quit()

w = gtk.Window()
w.connect("destroy", destroy)
w.show()
w.b = gtk.Button("Hello")
w.b.connect_object("clicked",hello, None)
w.add(w.b)
w.b.show()

gtk.main()
