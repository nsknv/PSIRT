

 NVIDIA SHIELD TV Security Updates for Multiple Vulnerabilities
=================================================================================




 Updated 09/29/2021 01:08 PM



NVIDIA SHIELD TV security updates for vulnerabilities that may lead to denial of service, information disclosure, or escalation of privileges
---------------------------------------------------------------------------------------------------------------------------------------------

 



---




### Vulnerability Details


The following sections summarize the potential vulnerabilities. Descriptions use [CWE™](https://cwe.mitre.org/) and risk assessments follow [CVSS](https://www.first.org/cvss/user-guide).


#### CVE-2017-6282


NVIDIA Tegra kernel driver contains a vulnerability in NVMAP where an attacker has the ability to write an arbitrary value to an arbitrary location, which may lead to an escalation of privileges.


CVSS Base Score: 9.3 
CVSS Temporal Score: 8.4 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6279


NVIDIA Tegra OpenMax Component contains a vulnerability in OMX.Nvidia.aac.decoder, which is not actively used or maintained, where disabling the dead code to avoid malicious software instantiates this component and may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.4 
CVSS Temporal Score: 7.6 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6295


NVIDIA TrustZone Software contains a vulnerability in the Keymaster implementation where the software reads data past the end, or before the beginning, of the intended buffer; and may lead to denial of service or information disclosure.


CVSS Base Score: 8.4 
CVSS Temporal Score: 7.3 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H/E:U/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H/E:U/RL:O/RC:C)


#### CVE-2017-13175


NVIDIA Tegra OpenMax Component contains a vulnerability in OMX.Nvidia.audio.render, which is not actively used or maintained, where there is the potential for mediaserver to reference memory after it has been freed which may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.0 
CVSS Temporal Score: 7.2 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6276


NVIDIA OpenMax Component contains a vulnerability in LIBNVMMLITE\_VIDEO.SO where there is the potential for mediaserver to reference memory after it has been freed, which may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 7.8 
CVSS Temporal Score: 7.0 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6283


NVIDIA Security Engine contains a vulnerability in the RSA function where the keyslot read/write lock permissions are cleared on a chip reset, which may lead to information disclosure.


CVSS Base Score: 7.1 
CVSS Temporal Score: 6.8 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:O/RC:C)


#### CVE-2017-6284


NVIDIA Security Engine contains a vulnerability in the Deterministic Random Bit Generator (DRBG) where the DRBG does not properly initialize and store or transmits sensitive data using a weakened encryption scheme that is unable to protect sensitive data, which may lead to information disclosure.


CVSS Base Score: 7.1 
CVSS Temporal Score: 6.8 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:O/RC:C)


#### CVE-2017-6296


NVIDIA TrustZone Software contains a TOCTOU issue in the DRM application which may lead to the denial of service or possible escalation of privileges.


CVSS Base Score: 5.5 
CVSS Temporal Score: 4.8 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N/E:U/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N/E:U/RL:O/RC:C)


*NVIDIA’s risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk of your specific configuration. NVIDIA doesn’t know of any exploits to these issues at this time.*


### Affected Software


| Product | OS | Versions |
|:----------|:--------|:-------------------|
| SHIELD TV | Android | SE 6.2 and earlier |
### Software Security Updates


Updates for SHIELD are available from **Settings** > **About** > **System update**.


| Product | OS | Updated Version |
|:----------|:--------|:------------------|
| SHIELD TV | Android | SE 6.3 |
**Notes:**


* Customers using earlier driver branches of this product should upgrade to one of the updated supported driver branches listed.
* SHIELD TV 6.3 also contains updates for CPU speculative side-channel vulnerabilities. For more information, see [Security Bulletin ID: 4613](http://nvidia.custhelp.com/app/answers/detail/a_id/4613).


### Mitigations


None.


### Acknowledgements


None.


### Get the Most Up to Date Product Security Information


To learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT), see the current list of NVIDIA security bulletins, or subscribe to security bulletin notifications, go to [NVIDIA Product Security](http://www.nvidia.com/product-security).


### Revision History


| Revision | Date | Description |
|-----------:|:------------------|:-----------------------------------------------------------------------------------------|
| 1.1 | March 13, 2018 | Corrected the introduction to the vulnerability descriptions to state that they use CWE. |
| 1 | February 15, 2018 | Initial release |
##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA Jetson TX1, Jetson TK1, Jetson TX2, and Tegra K1 L4T Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4635/related/1)
* [ NVIDIA Shield TV and Tablet contain multiple vulnerabilities](/app/answers/detail/a_id/4548/related/1)
* [ NVIDIA GPU Display Driver Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4649/related/1)
* [ NVIDIA Driver Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4611/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)








