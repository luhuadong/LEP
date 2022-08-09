/* vi: set sw=4 ts=4: */
/*
 *
 * dmesg - display/control kernel ring buffer.
 *
 * Copyright 2006 Rob Landley <rob@landley.net>
 * Copyright 2006 Bernhard Reutner-Fischer <rep.nop@aon.at>
 *
 * Licensed under GPLv2, see file LICENSE in this source tree.
 */

//usage:#define dmesg_trivial_usage
//usage:       "[-c] [-n LEVEL] [-s SIZE]"
//usage:#define dmesg_full_usage "\n\n"
//usage:       "Print or control the kernel ring buffer\n"
//usage:     "\n	-c		Clear ring buffer after printing"
//usage:     "\n	-n LEVEL	Set console logging level"
//usage:     "\n	-s SIZE		Buffer size"

#include <sys/klog.h>
#include "libbb.h"

int dmesg_main(int argc, char **argv, int fd) //MAIN_EXTERNALLY_VISIBLE;
//int dmesg_main(int argc UNUSED_PARAM, char **argv)
{
	int len = 2048, level;
	char *buf;
	unsigned opts = 0;
	enum {
		OPT_c = 1 << 0,
		OPT_s = 1 << 1,
		OPT_n = 1 << 2
	};

	FILE *fp = fdopen(fd, "w");
	if(fp == NULL) return EXIT_SUCCESS;

	opt_complementary = "s+:n+"; /* numeric */
	opts = getopt32(argv, "cs:n:", &len, &level);
	if (opts & OPT_n) {
		if (klogctl(8, NULL, (long) level))
			bb_perror_msg_and_die("klogctl");
		return EXIT_SUCCESS;
	}

#if 0
	if (!(opts & OPT_s))
		len = klogctl(10, NULL, 0); /* read ring buffer size */
	if (len < 16*1024)
		len = 16*1024;
	if (len > 16*1024*1024)
		len = 16*1024*1024;
#endif
	buf = malloc(len);
	len = klogctl(3 + (opts & OPT_c), buf, len); /* read ring buffer */
	if (len < 0)
		//bb_perror_msg_and_die("klogctl");
		goto exit;
	if (len == 0)
		//return EXIT_SUCCESS;
		goto exit;


	//if (ENABLE_FEATURE_DMESG_PRETTY) {
	if (0) {
		int last = '\n';
		int in = 0;

		/* Skip <[0-9]+> at the start of lines */
		while (1) {
			if (last == '\n' && buf[in] == '<') {
				while (buf[in++] != '>' && in < len)
					;
			} else {
				last = buf[in++];
				putchar(last);
			}
			if (in >= len)
				break;
		}
		/* Make sure we end with a newline */
		if (last != '\n')
			bb_putchar('\n');
	} else {
		//full_write(STDOUT_FILENO, buf, len);
		//if (buf[len-1] != '\n')
			//bb_putchar('\n');
		fprintf(fp,"%s\n",buf);
	}

	//if (ENABLE_FEATURE_CLEAN_UP) free(buf);
exit:
	free(buf);
	fclose(fp);
	return EXIT_SUCCESS;
}
