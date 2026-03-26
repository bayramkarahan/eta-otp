#!/bin/bash

langs=$(cat po/LINGUAS)

if ! command -v xgettext &> /dev/null
then
	echo "xgettext could not be found."
	echo "you can install the package with 'apt install gettext' command on debian."
	exit
fi


echo "updating pot file"
xgettext -o po/eta-otp-lock.pot \
     --from-code="utf-8" \
    `find src -type f -iname "*.py"`


for lang in ${langs[@]}; do
	if [[ -f po/$lang.po ]]; then
		echo "updating $lang.po"
		msgmerge -o po/$lang.po po/$lang.po po/eta-otp-lock.pot
	else
		echo "creating $lang.po"
		cp po/eta-otp-lock.pot po/$lang.po
	fi
done
