#!/usr/bin/env python3
import os
import pyotp
import json

CONFIG_FILE = "/etc/otp-secrets.json"

def pam_sm_authenticate(pamh, flags, argv):
    # fetch OTP
    if pamh.authtok is None:
        try:
            conv = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "Password: "))
            pamh.authtok = conv.resp
        except:
            return pamh.PAM_AUTH_ERR

    # read config
    if not os.path.isfile(CONFIG_FILE):
        return pamh.PAM_AUTH_ERR
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)

    if 'global' in config:
        otp = pyotp.TOTP(config['global'])
        if otp.now() == pamh.authtok:
            return pamh.PAM_SUCCESS

    return pamh.PAM_AUTH_ERR

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS
