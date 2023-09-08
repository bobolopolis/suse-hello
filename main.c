/*
* main.c - A demo kernel module.
*
* Copyright (C) 2003, 2004, 2005, 2006
* Andreas Gruenbacher <agruen@suse.de>, SUSE Labs
*
* This program is free software; you can redistribute it and/or
* modify it under the terms of the GNU General Public License as
* published by the Free Software Foundation.
*
* A copy of the GNU General Public License can be obtained from
* http://www.gnu.org/.
*/

#include <linux/module.h>
#include <linux/init.h>

MODULE_AUTHOR("Andreas Gruenbacher <agruen@suse.de>");
MODULE_DESCRIPTION("Hello world module");
MODULE_LICENSE("GPL");

int param;

module_param(param, int, 0);
MODULE_PARM_DESC(param, "Example parameter");

void exported_function(void)
{
	printk(KERN_INFO "Exported function called.\n");
}
EXPORT_SYMBOL_GPL(exported_function);

int __init init_hello(void)
{
	printk(KERN_INFO "Hello world.\n");
	return 0;
}

void __exit exit_hello(void)
{
	printk(KERN_INFO "Goodbye world.\n");
}

module_init(init_hello);
module_exit(exit_hello);
