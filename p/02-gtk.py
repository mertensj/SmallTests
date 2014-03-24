#!/usr/bin/python2
#
# http://www.pygtk.org/pygtk2tutorial/index.html
#
import gtk
import pygtk
# 
#
def hello(data=None):
	print "Hello ..."

def destroy(data=None):
	gtk.main_quit()

def callback(data):
	print "Hello - %s was pressed." % data

w = gtk.Window()
w.connect("destroy", destroy)
w.set_border_width(10)

# Create a box to pack widgets
box1=gtk.HBox(False, 0)

b1 = gtk.Button("Knop 1")
b2 = gtk.Button("Knop 2")
b3 = gtk.Button("Knop 3")
b4 = gtk.Button("Knop 4")
b1.connect_object("clicked",callback, "knop 1")
b2.connect_object("clicked",callback, "knop 2")
b3.connect_object("clicked",callback, "knop 3")
b4.connect_object("clicked",callback, "knop 4")

box1.pack_start(b1, True, True, 0)
box1.pack_start(b2, True, True, 0)
box1.pack_start(b3, True, True, 0)
box1.pack_start(b4, True, True, 0)

b1.show()
b2.show()
b3.show()
b4.show()

box1.show()
w.add(box1)
w.show()

gtk.main()
