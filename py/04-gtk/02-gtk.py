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

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
#w.set_title("Example")
w.set_size_request(300,300)
w.connect("destroy", destroy)
w.set_border_width(10)

# Create a Frame
frame = gtk.Frame()
#w.add(frame)
frame.set_label("Example Frame")
frame.set_label_align(1.0, 0.0)
frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
frame.show()

# Create a box to pack widgets
box0=gtk.VBox(False, 0)
box1=gtk.HBox(False, 0)
box2=gtk.HBox(False, 0)

b1 = gtk.Button("Knop 1")
b2 = gtk.Button("Knop 2")
b3 = gtk.Button("Knop 3")
b4 = gtk.Button("Knop 4")
bQ = gtk.Button("Quit")
b1.connect_object("clicked",callback, "knop 1")
b2.connect_object("clicked",callback, "knop 2")
b3.connect_object("clicked",callback, "knop 3")
b4.connect_object("clicked",callback, "knop 4")
bQ.connect_object("clicked",destroy, None)

box1.pack_start(b1, True, True, 0)
box1.pack_start(b2, True, True, 0)
box1.pack_start(b3, True, True, 0)
box1.pack_start(b4, True, True, 0)

b1.show()
b2.show()
b3.show()
b4.show()

box2.pack_start(bQ, True, False, 0)
bQ.show()

box0.pack_start(box1, False, False, 0)
separator = gtk.HSeparator()
box0.pack_start(separator, False, True, 5)
separator.show()
box0.pack_start(box2, False, False, 0)
box2.show()
box0.add(frame)

box1.show()
box0.show()
w.add(box0)
w.show()

gtk.main()
