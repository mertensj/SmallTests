#include <stdlib.h>
#include <gtk/gtk.h>

int main(int argc, char *argv[])
{
 GtkStatusIcon *MyIcon;
 printf("..... Hi ..... :)  \n");
 gtk_init(&argc, &argv);

 MyIcon = gtk_status_icon_new();
 /* MyIcon = gtk_status_icon_new_from_file("~/tst/web.png");
 */
 gtk_status_icon_set_visible(MyIcon, TRUE);

 update_tray_icon (MyIcon);

 gtk_main();

 return 0;
}
