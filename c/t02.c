/* COMPILE USING:  gcc -Wextra -o cairo1 `pkg-config --cflags --libs gtk+-3.0` cairo1.c */
#include <gtk/gtk.h>

#define WINDOW_WIDTH  300
#define WINDOW_HEIGHT 300
#define BLUE 0,0,255
#define RED 0.77, 0.16, 0.13
#define WIDTH 3

static gboolean draw_cb(GtkWidget *widget, cairo_t *cr, gpointer data)
{   
   /* Set color for background */
   /* cairo_set_source_rgb(cr, 1, 1, 1); */
   /* fill in the background color*/
   /* cairo_paint(cr); */

   /* draw horizontal line */
   cairo_set_source_rgb(cr, BLUE);
   cairo_set_line_width(cr, WIDTH);
   cairo_move_to(cr, 80,160);
   cairo_line_to(cr, 200, 160);
   cairo_stroke(cr);

   return FALSE;
}

int main (int argc, char *argv[])
{
   GtkWidget *window;
   GtkWidget *da;

   gtk_init (&argc, &argv);

   window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
   g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);

   da = gtk_drawing_area_new();
   gtk_widget_set_size_request (da, WINDOW_WIDTH, WINDOW_HEIGHT);
   g_signal_connect (da, "draw", G_CALLBACK(draw_cb),  NULL);

   gtk_container_add (GTK_CONTAINER (window), da);
   gtk_widget_show(da);
   gtk_widget_show (window);

   gtk_main ();

   return 0;
}
