import telebot
from telebot import types

names = {
	
	'master': ['BQACAgQAAxkBAAITdmAXl1HOMtXIrC1FQ_q4nsfDKI7yAAJCCgACVmaZUDE6GNbE8hVDHgQ',
			   'BQACAgQAAxkBAAITd2AXl1HFxsUx-BPNVbC0gnavv_qVAAK1BwACOG2YUFy83wknBEkIHgQ',
			   'BQACAgQAAxkBAAITeGAXl1GAV9hXu60h6ohWlzQ6fMkuAAK2BwACOG2YUH-FZjU-UjwKHgQ',
			   'BQACAgQAAxkBAAITeWAXl1HPVIL5SgErAkxyHH4bJMOzAAIgCQACVzGgUPpuO70aTP5zHgQ',
			   'BQACAgQAAxkBAAITemAXl1Eyi9WKw3eKQMkLAsq43lISAAIfCQACVzGgUI9zuj-6Y98JHgQ',
			   'Master 2021 Telugu HDRip'
	],
			   
	'krack' : ['BQACAgQAAxkBAAIcRmAcsoh_IUhbt3pN6fjgSdlMissyAALcCAAC2lrpUHZNnzBop7HUHgQ',
			   'BQACAgQAAxkBAAIcR2Acsoj5kbLSINPtgXSLV3BpcZKfAALfCAAC2lrpUKjTWiBoBQyLHgQ',
			   'BQACAgQAAxkBAAIcSGAcsoiXSalsE7qQdAeoRa54lKARAALiCAAC2lrpUCG_81OJpY7MHgQ',
			   'BQACAgQAAxkBAAIcSWAcsogCFfp1dUWKogZAWrZFQZptAAL4CgACIxfpUCXQSsULrLgpHgQ',
			   'BQACAgQAAxkBAAIcSmAcsojiCHIT5GiIRsj-tqQ1HpY9AALkCAAC2lrpULS8NjXBhrS1HgQ',
			   'Krack 2021 Telugu HDRip'
	],
	
	'rangde' : ['BQACAgQAAxkBAAI0dmBq0F5AwEMRifIEygiEe8gR2puZAAKLCQACP7TwUufxCYSqDGE9HgQ',
			    'BQACAgQAAxkBAAI0d2Bq0F7Hy7hWVHgsnyZcTv9Ul-0mAAJ9CQACP7TwUkIN7GTFOB0QHgQ',
		 	   'BQACAgQAAxkBAAI0eGBq0F5ldoGhavnbvP_ZtAo09cvbAAJ-CQACP7TwUtnjMIiXCSWeHgQ',
	 		   'BQACAgQAAxkBAAI0eWBq0F5DiWD-oawSj69Cbu0C1kSMAAJ8CQACP7TwUrx4OyRF2M1iHgQ',
		 	   'BQACAgQAAxkBAAI0emBq0F67iawXa_JgaLs1GR1W7eZ_AAJ5CQACP7TwUvhycAlvq7nOHgQ',
			    'Rang De! 2021 Telugu DVDRip'
	],
	
	'sbsb'  : ['BQACAgQAAxkBAAITkmAXowag3DFChGScDlUrDMAruaBwAAIkDgACVGV5UzeMNg6c6SGsHgQ',
			   'BQACAgQAAxkBAAITk2AXowZr4u3JuBr4Y38giMSHhuojAAImDgACVGV5U8iwDfhrflEaHgQ',
			   'BQACAgQAAxkBAAITlGAXowavfPmqPZQ-jX55pMuxZFV-AAIqCQACUwR5U9UHPvg638ETHgQ',
			   '0',
			   'BQACAgQAAxkBAAITlWAXowa4ZwrB3xeh4NxhXiwm-2YlAAIoCQACUwR5U2cb738s_CchHgQ',
			   'Solo Brathuke So Better 2021 Telugu HDRip'
	],
	
	'red'   : ['BQACAgQAAxkBAAInSmA0WaEf-aUhjX8sOeRWGSiUght0AAK4DAACJIKhUSzlue2PralHHgQ',
			   'BQACAgQAAxkBAAInS2A0WaFHAAE5u4QEKWZOgofcn3zoUQACvgwAAiSCoVEwmFPP7EcmsR4E',
			   'BQACAgQAAxkBAAInTGA0WaFfHNFfo54sel8dav_WHQvcAAK9DAACJIKhUT5qJgnpXPpLHgQ',
			   'BQACAgQAAxkBAAInfGA1FW3UhzUwBtyswHPNA-OwjVoCAALUCQAC9yepUR9-TP28S7uGHgQ',
			   'BQACAgQAAxkBAAInfWA1FW183NyVOx4BxOy_-ztCh7MRAAL4CAAC9yexUVGj4XV47RTMHgQ',
			   'Red 2021 Telugu HDRip'
	],
	
	'vakeelsaab':
			 ['BQACAgQAAxkBAAI_EmCL90he2Xca0mUNfFI1FmXq4br2AAKlCQACmzxZUKZDUd_T8JxNHwQ',
			  'BQACAgQAAxkBAAI_EWCL90g4Av8Vg1V4zTW_fKMWSON9AAKmCQACmzxZUKvrj7qyqwNMHwQ',
			  'BQACAgQAAxkBAAI_EGCL90jcYYCyga14ptKk1cReIiHLAAKpCQACmzxZUKsPbFX77xD6HwQ',
		 	 'BQACAgQAAxkBAAI_D2CL90j_IfDTsQ5fjne-jpttKFmeAAKoCQACmzxZUPQ1n2NluzpEHwQ',
			  'BQACAgQAAxkBAAI_DmCL90gqnP617vXqKLxEa-Hblb7oAAKnCQACmzxZUGzEYMPdcFIfHwQ',
		 	 'Vakeel Saab 2021 Telugu HDRip'		  
	],
	
	'alluduadhurs'  :
			 ['BQACAgQAAxkBAAIksWAnrv0_yWZLvxI8pOsRh2s3f90LAALQCQACUI85URIVr6qAWYoGHgQ',
			  'BQACAgQAAxkBAAIksmAnrv0hsBON2lQeDK9btb4oybw-AALNCQACUI85UbHtgxYG24DoHgQ',
			  'BQACAgQAAxkBAAIks2Anrv1YX8TmqMp8J6yVL-J92snxAAIZDQACEIs5UcqWeiTZ0OWJHgQ',
			  'BQACAgQAAxkBAAITrWAXqENLx6PkfYRESDAuCNuTkyk0AAIbCQACocAIUFUYcmX-q9zUHgQ',
			  'BQACAgQAAxkBAAIk32AnsWmBzlKrEALHxTFrtjl7uBgxAALnDQACEIs5UYKOcQzoDXA5HgQ',
			  'Alludu Adhurs 2021 Telugu HDRip'
	],
	
	'aranya': ['BQACAgQAAxkBAAI0lGBq0x6SyHY42h83xGrYKsge3h6rAAK8CgACXArxUhHAHekpwLDpHgQ',
			   'BQACAgQAAxkBAAI0lWBq0x7s3vVMnA9Wu8NLMfkbLf3jAAKrCgACXArxUh5FcfNRkyjMHgQ',
			   'BQACAgQAAxkBAAI0lmBq0x4Q0W-MJQacm0xGYd0T_Lt7AAKyCgACXArxUuk6ud5eISBNHgQ',
			   'BQACAgQAAxkBAAI0l2Bq0x4jTGBN08poNit9KevEgTffAAKxCgACXArxUrFYmvVK9UxhHgQ',
			   'BQACAgQAAxkBAAI0mGBq0x7YxuPJny7c4h8TYSwFlv7wAAK1CgACXArxUrC6qmdKrRNaHgQ',
			   'Aranya 2021 Telugu DVDRip'
	],
	
	'shashi': ['BQACAgQAAxkBAAI_bWCL-6CyMFuqTVggfq9DHHDZ7oQgAAJZCQACnoLBU3R7VfbGQAABqR8E',
			   'BQACAgEAAxkBAAI_bmCL-6BUZziTvkJBo8PAua25GZlZAALOAQACKsHAR6IR1OwzqDXlHwQ',
			   'BQACAgQAAxkBAAI_b2CL-6BnQY9v0VqHeFSS2la421CKAAIVDQAC2gu4U1ApJeKk0j-QHwQ',
			   '0',
			   'BQACAgQAAxkBAAI_cGCL-6D3i-KhFqfrw9iHk6e-4K_sAAJgCwACHgABuFPCtasSM7LE-B8E',
			   'Shashi 2021 Telugu HDRip'
	],
	
	'check': ['BAACAgQAAxkBAAIpU2A9AboouCMnJkbsyHNubQYrp75MAAIiEgACOwrJUfKYz0SsIEnSHgQ',
			  'BAACAgQAAxkBAAIpVGA9Abr6sWKNHgABncmjhqIoZeDKnAACBBIAAjsKyVH8sVQWSYMeSB4E',
			  'BAACAgQAAxkBAAIpVWA9Abo5shSmgRUQiqauI2EYIGwBAAIBCAACqYLIUVKJKydcRbJdHgQ',
			  'BAACAgQAAxkBAAIpVmA9AboGjuIf-P80ULwleRsJdqHxAALsCAACpGPIUWCf0b7tc4n6HgQ',
			  'BAACAgQAAxkBAAIpV2A9AbqIPUa_LfvbamUD77VfsFJwAAJ_CgACD1TAUV-d6p5nQGJ2HgQ',
			  'Check 2021 Telugu DVDRip',
			  'video'
	],
	
	'jathiratnalu':	 
			  ['BQACAgQAAxkBAAI_WWCL-ngKxcCQL6iWstS3uv8-mOidAAIrCwACSRaxUyB0-zCoXRlvHwQ',
			   'BQACAgQAAxkBAAI_WmCL-nhDHy6URWwMUKX5hfjVkIUrAAI2CwACSRaxU23FOt9v91yoHwQ',
			   'BQACAgQAAxkBAAI_W2CL-ng7XpNtAAFTenyyoHndEI5yxgACNwsAAkkWsVOH63MmnKxSXh8E',
			   'BQACAgQAAxkBAAI_XGCL-ngZhEzxOl-e37qxoTf6tWn_AAJDCwACSRaxU4nObyB-tbuqHwQ',
			   'BQACAgQAAxkBAAI_XWCL-nhJiDi9doTZ7pjBp3j1_yiDAAJFCwACSRaxUyuAYekX3I7jHwQ',
			   'Jaathiratnalu 2021 Telugu HDRip'
	],
	
	'sreekaram':
			  ['BQACAgQAAxkBAAI_RWCL-bKguYAKAtlkbSBX84j_krU3AAJGCAACLvHIU2kcR21QlFAOHwQ',
			   'BQACAgQAAxkBAAI_RmCL-bJllPxz6jvz_UkPA3uh4EaKAALXBgACnZ7JU6d0WfhI2CqVHwQ',
			   'BQACAgQAAxkBAAI_R2CL-bIFKIcO_7R2t9ADKXeM4oU0AAIeBwACThDIU5trJUApAzriHwQ',
			   'BQACAgQAAxkBAAI_SGCL-bKO6szYqkp4eNxAGS_yvjfgAAJHCAACLvHIUwyYstB4iVgvHwQ',
			   'BQACAgQAAxkBAAI_SWCL-bL5RmVkMPme5Krm08Crk2nnAAJLCAACLvHIU20OIs2oTzr9HwQ',
			   'Sreekaram 2021 Telugu HDRip'
	
	],
	
	'uppena' :['BQACAgQAAxkBAAI_MWCL-T6NGocjwYbZbHMePbe8EJc2AAK1CgACXnCxU4BE1A_9r_FjHwQ',
			   'BQACAgQAAxkBAAI_MmCL-T574vhs9kyHA1_U4byGC0KoAAJICAACCIS4U55FVYmpo1q0HwQ',
			   'BQACAgQAAxkBAAI_M2CL-T5jAZt_oX1xb9arSYzpdcAWAAIbCQAC2SqwU_qPTBuZrTOyHwQ',
			   'BQACAgQAAxkBAAI_NGCL-T7uiUD8gkYEk--JnPUFuByBAAK2CgACXnCxUxAPlmxoFaprHwQ',
			   'BQACAgQAAxkBAAI_NWCL-T5HkUkMklv37k-UEvGOR7KBAAL7CAACqSWxU6kd9q-Ic2nNHwQ',
			   'Uppena 2021 Telugu HDRip'
	],
	
	'pogaru' :['BQACAgQAAxkBAAInvGA3CAN7Fh8Y7FX109GDNbiFF6YlAALiCAAC6HeIURbnC6otHIoGHgQ',
			   'BQACAgQAAxkBAAInvWA3CAMhgsCmONRP45Zep0UJn72kAAI7CQAC6HeIUfiTapnSeY8kHgQ',
			   'BQACAgQAAxkBAAInvmA3CAN7B4V4VZ7ZPsX1ux9tqzguAAI-CQAC6HeIUSNxzhesX57QHgQ',
			   '0',
			   'BQACAgQAAxkBAAInv2A3CAN53n0Qud5K1WF78YWycJ5TAAJGCQAC6HeIUcPP058L2n-gHgQ',
			   'Pogaru 2021 Telugu PreDVD'
	],
	
	'sulthan':['BQACAgQAAxkBAAI_fmCL_PH-y8B9XiLtia8Qt5jiUsNzAAKfCQACmzxZUKb9Ron-85aiHwQ',
			   'BQACAgQAAxkBAAI_f2CL_PFS-L-Tnw1whlia8gxHfMC1AAKeCQACmzxZUIPVLeYnjsMfHwQ',
			   'BQACAgQAAxkBAAI_gGCL_PFcD5H8Yjl5GWbbdhJaKmGPAAKgCQACmzxZUAi9xlgY72BcHwQ',
			   'BQACAgQAAxkBAAI_gWCL_PHaM-Yfx64pZU58k6dyBMp9AAKhCQACmzxZUKdVmZpY5EcbHwQ',
			   'BQACAgQAAxkBAAI_gmCL_PEx6RNz3DaUy3tSIkqemCJQAAKiCQACmzxZUGoKvM3xAwkGHwQ',
			   'Sulthan 2021 Telugu HDRip'
	],

}

def moviecheck(a):
	if a=="m1":
		b="master"
	elif a=="m2":
		b="krack"
	elif a=="m3":
		b="rangde"
	elif a=="m4":
		b="sbsb"
	elif a=="m5":
		b="red"
	elif a=="m6":
		b="vakeelsaab"
	elif a=="m7":
		b="alluduadhurs"
	elif a=="m8":
		b="aranya"
	elif a=="m9":
		b="shashi"
	elif a=="m10":
		b="check"
	elif a=="m11":
		b="jathiratnalu"
	elif a=="m12":
		b="sreekaram"
	elif a=="m13":
		b="uppena"
	elif a=="m14":
		b="pogaru"
	elif a=="m15":
		b="sulthan"
	else:
		b=""
	return b

def sizecheck(a):
	if a=="s1":
		b=0
	elif a=="s2":
		b=1
	elif a=="s3":
		b=2
	elif a=="s4":
		b=3
	elif a=="s5":
		b=4
	elif a=="s0":
		b="a"
	else:
		b=5
	return b

def msize(a):
	if a==0:
		b="200MB 220p"
	elif a==1:
		b="400MB 360p"
	elif a==2:
		b="700MB 480p"
	elif a==3:
		b="900MB 720p"
	elif a==4:
		b="1.4GB 1080p FHD"
	else:
		b="Unknown"
	return b

key = {
		  "inline_keyboard": [
						[
							{"text": "Master", "callback_data": "m1"},
						],
						[
							{"text": "Krack", "callback_data": "m2"},
						],
						[
							{"text": "Rang De!", "callback_data": "m3"},
						],
						[
							{"text": "Solo Brathuke So Better", "callback_data": "m4"},
						],
						[
							{"text": "Red", "callback_data": "m5"},
						],
						[
							{"text": "Vakeel Saab", "callback_data": "m6"},
						],
						[
							{"text": "Alludu Adhurs", "callback_data": "m7"},
						],
						[
							{"text": "Aranya", "callback_data": "m8"},
						],
						[
							{"text": "Shashi", "callback_data": "m9"},
						],
						[
							{"text": "Check", "callback_data": "m10"}
						],
						[
							{"text": "Jaathiratnalu", "callback_data": "m11"},
						],
						[
							{"text": "Sreekaram", "callback_data": "m12"},
						],
						[
							{"text": "Uppena", "callback_data": "m13"},
						],
						[
							{"text": "Pogaru", "callback_data": "m14"},
						],
						[
							{"text": "Sulthan", "callback_data": "m15"},
						],
						[
							{"text": "❌ Cancel ❌", "callback_data": "clear"},
						],
					]
	  }

key1 = types.InlineKeyboardMarkup(row_width=3)
a = types.InlineKeyboardButton(text="Master", callback_data="m1")
b = types.InlineKeyboardButton(text="Krack", callback_data="m2")
c = types.InlineKeyboardButton(text="Rang De!", callback_data="m3")
d = types.InlineKeyboardButton(text="Solo Brathuke So Better", callback_data="m4")
e = types.InlineKeyboardButton(text="Red", callback_data="m5")
f = types.InlineKeyboardButton(text="Vakeel Saab", callback_data="m6")
g = types.InlineKeyboardButton(text="Alludu Adhurs", callback_data="m7")
h = types.InlineKeyboardButton(text="Aranya", callback_data="m8")
i = types.InlineKeyboardButton(text="Shashi", callback_data="m9")
j = types.InlineKeyboardButton(text="Check", callback_data="m10")
k = types.InlineKeyboardButton(text="Jathiratnalu", callback_data="m11")
l = types.InlineKeyboardButton(text="Sreekaram", callback_data="m12")
m = types.InlineKeyboardButton(text="Uppena", callback_data="m13")
n = types.InlineKeyboardButton(text="Pogaru", callback_data="m14")
o = types.InlineKeyboardButton(text="Sulthan", callback_data="m15")
p = types.InlineKeyboardButton(text="❌ Cancel ❌", callback_data="clear")

key1.add(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

	
def sizekeyedit(a):
	  
	sizekey = {
		  "inline_keyboard": [
						[
							{"text": "All Qualities", "callback_data": a+" s0"},
						],
						[
							{"text": "220p", "callback_data": a+" s1"},
						
						
							{"text": "360p", "callback_data": a+" s2"},
						],
						[
							{"text": "480p", "callback_data": a+" s3"},
						
						
							{"text": "720p MHD", "callback_data": a+" s4"},
						],
						[
							{"text": "1080p FHD", "callback_data": a+" s5"},
						
						
							{"text": "<< Go Back", "callback_data": "m0"},
						],
						[
							{"text": "❌ Cancel ❌", "callback_data": "clear"},
						],
					]
	  }
	return sizekey
