# Security Notice: NVIDIA Response to Security Incident (Bulletin ID: 5333)



Security Notice: NVIDIA Response to Security Incident - March 2022
==================================================================




 Updated 03/08/2022 10:50 AM



Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Update March 8, 2022:


The two NVIDIA code-signing certificates that were reported to be leaked in this cybersecurity incident are expired:


subject CN: NVIDIA Corporation  

issuer CN: VeriSign Class 3 Code Signing 2010 CA  

serial: 43bb437d609866286dd839e1d00309f5  

valid from: ‎September ‎1, ‎2011  

valid to: ‎September ‎1, ‎2014
And:


subject CN: NVIDIA Corporation  

issuer CN: VeriSign Class 3 Code Signing 2010 CA  

serial: 14781bc862e8dc503a559346f5dcc518  

valid from: ‎July ‎27, ‎2015  

valid to: ‎‎July ‎26, ‎2018
Criminal actors might include these expired certificates in malicious code that has been fraudulently signed, creating the misimpression that the code came from NVIDIA.  We recommend that customers run NVIDIA software provided only from our trusted, legitimate sources. Also, NVIDIA recommends following the industry best practice of not trusting any certificates beyond their expiration date.


### March 1, 2022:


On February 23, 2022, NVIDIA became aware of a cybersecurity incident which impacted IT resources. Shortly after discovering the incident, we further hardened our network, engaged cybersecurity incident response experts, and notified law enforcement.


We have no evidence of ransomware being deployed on the NVIDIA environment or that this is related to the Russia-Ukraine conflict. However, we are aware that the threat actor took employee passwords and some NVIDIA proprietary information from our systems and has begun leaking it online. Our team is working to analyze that information. All employees have been required to change their passwords. We do not anticipate any disruption to our business or our ability to serve our customers as a result of the incident.


Security is a continuous process that we take very seriously at NVIDIA – and we invest in the protection and quality of our code and products daily.


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 2.0 | March 8, 2022 | Added expired certificate information |
| 1.0 | March 1, 2022 | Initial release |


### Support


If you have any questions about this security notice, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GeForce Experience - December 2021](/app/answers/detail/a_id/5295/related/1)
* [ NVIDIA Omniverse Launcher - January 2022](/app/answers/detail/a_id/5318/related/1)
* [ NVIDIA SHIELD TV - January 2022](/app/answers/detail/a_id/5259/related/1)
* [ NVIDIA License System - February 2022](/app/answers/detail/a_id/5319/related/1)
* [Security Notice: NVIDIA Response to Log4j Vulnerabilities - December 2021](/app/answers/detail/a_id/5294/related/1)








