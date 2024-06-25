

 NVIDIA Jetson TX1, Jetson TK1, Jetson TX2, and Tegra K1 L4T Security Updates for Multiple Vulnerabilities
============================================================================================================================




 Updated 09/29/2021 01:08 PM



Jetson and Tegra L4T contain vulnerabilities which may lead to denial of service, escalation of privileges, or information disclosure.
--------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](http://www.nvidia.com/object/product-security.html).
------------------------------------------------------------------------------------






---




### Vulnerability Details


The following sections summarize the potential vulnerabilities. Descriptions use [CWE™](https://cwe.mitre.org/) and risk assessments follow [CVSS](https://www.first.org/cvss/user-guide).


#### CVE-2017-6282


NVIDIA Tegra kernel driver contains a vulnerability in NVMAP where an attacker has the ability to write an arbitrary value to an arbitrary location, which may lead to an escalation of privileges.


CVSS Base Score: 9.3 
CVSS Temporal Score: 8.4 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=A/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/R)


#### CVE- 2017-6248


NVIDIA Tegra kernel audio driver contains a vulnerability in Audio Digital Signal Processor (DSP) in the case of invalid user parameter, leading to denial of service or escalation of privileges.


CVSS Base Score: 9.2 
CVSS Temporal Score: 8.3 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:H/E:P/RL:O/RC:C)


#### CVE-2017-0328


NVIDIA Tegra kernel driver contains a vulnerability in NVIDIA crypto where software does not terminate or incorrectly terminates a string or array with a null character or equivalent terminator, which may lead to denial of service.


CVSS Base Score: 9.0 
CVSS Temporal Score: 8.1 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:H/E:P/RL:O/RC:C)


#### CVE-2016-6776


NVIDIA Tegra kernel driver contains a vulnerability in the NVHOST driver where referencing memory after it has been freed may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.4 
CVSS Temporal Score: 7.6 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6275


NVIDIA Tegra kernel contains a vulnerability in the CORE DVFS Thermal driver where there is the potential to read or write a buffer using an index or pointer that references a memory location after the end of the buffer, which may lead to a denial of service or possible escalation of privileges.


CVSS Base Score: 8.4 
CVSS Temporal Score: 7.6 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6278


NVIDIA Tegra kernel contains a vulnerability in the CORE DVFS Thermal driver where there is the potential to read or write a buffer using an index or pointer that references a memory location after the end of the buffer, which may lead to a denial of service or possible escalation of privileges.


CVSS Base Score: 8.4 
CVSS Temporal Score: 7.6 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-6276


NVIDIA Tegra OpenMax Component contains a vulnerability in LIBNVMMLITE\_VIDEO.SO, where the media server may be referencing memory after it has been freed, which may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 7.8 
CVSS Temporal Score: 7.0 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2017-0339


NVIDIA Tegra crypto-dev driver contains a vulnerability in the handling of IOCTLs in which a value is passed to the kernel driver without validation possibly causing array index issues, which may lead to information disclosure, denial of service, or code execution.


CVSS Base Score: 7.8 
CVSS Temporal Score: 6.8 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C)


#### CVE-2017-6283


NVIDIA Security Engine contains a vulnerability in the RSA function where the keyslot read/write lock permissions are cleared on a chip reset, which may lead to information disclosure.


CVSS Base Score: 7.1 
CVSS Temporal Score: 6.8 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:T/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:X/RL:T/RC:C)


#### CVE-2017-0448


NVIDIA Tegra kernel driver contains a vulnerability in NVHOST where referencing memory after it has been freed may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 7.1 
CVSS Temporal Score: 6.4 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N/E:P/RL:O/RC:C)


#### CVE-2017-6274


NVIDIA Tegra kernel contains a vulnerability in the CORE DVFS Thermal driver where there is the potential to read or write a buffer using an index or pointer that references a memory location after the end of the buffer, which may lead to a denial of service or possible escalation of privileges.


CVSS Base Score: 6.7 
CVSS Temporal Score: 6.0 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


*NVIDIA’s risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk of your specific configuration. NVIDIA doesn’t know of any exploits to these issues at this time.*


### Affected Software


The following table lists supported software versions and driver branches that are affected by the issues described in this bulletin. For available security updates, see [Software Security Updates](#software-security-updates).


Note that the table may not be a comprehensive list of all impacted software versions or driver branches and may be updated as more information becomes available. For the latest information, check for updates to this bulletin or go to [NVIDIA Product Security](http://www.nvidia.com/product-security) to subscribe to security bulletin notifications.


Additionally, support may have expired for certain software versions or driver branches. For information about software versions or driver branches that are no longer supported, contact [NVIDIA Support](http://www.nvidia.com/object/support.html) with any questions.


| CVEs | Product | OS | Version |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|:----------------|:----------------------------------------|
| CVE-2017-0328 CVE-2017-0339 CVE-2017-6248 CVE-2017-6274 CVE-2017-6275 CVE-2017-6276 CVE-2017-6278 CVE-2017-6282 CVE-2017-6283 | Jetson TX1 | Linux for Tegra | BSP 24.2.2 and prior BSP 28.1 and prior |
| CVE-2017-6282 CVE-2017-6283 CVE-2017-6274 CVE-2017-6275 | Jetson TX2 | Linux for Tegra | BSP 28.1 and prior |
| CVE-2016-6776 CVE-2017-0328 CVE-2017-0339 CVE-2017-0448 CVE-2017-6248 CVE-2017-6274 CVE-2017-6275 CVE-2017-6276 CVE-2017-6278 CVE-2017-6282 CVE-2017-6283 | Jetson TK1 and Tegra K1 | Linux for Tegra | BSP 21.6 and prior |
### Software Security Updates


The following supported software versions contain the security updates for the issues described in this bulletin. If you are using an unsupported software version or on an earlier driver branch that is no longer supported, upgrade to one of the updated supported versions listed.


| Product | OS | Updated Version |
|:--------------------------|:----------------|:---------------------|
| Jetson TX1 | Linux for Tegra | BSP 24.2.3 BSP R28.2 |
| Jetson TX1 and Jetson TX2 | Linux for Tegra | BSP R28.2 |
| Jetson TK1 and Tegra K1 | Linux for Tegra | BSP 21.7 |
**Notes**


* When available, download updates from [NVIDIA DevZone](https://developer.nvidia.com/embedded/downloads).
* NVIDIA Jetson TX1, Jetson TK1, Jetson TX2, and Tegra K1 L4T also contain updates for CPU speculative side channel vulnerabilities. For more information, see [Security Bulletin ID: 4616](http://nvidia.custhelp.com/app/answers/detail/a_id/4616) and [Security Bulletin ID: 4617](http://nvidia.custhelp.com/app/answers/detail/a_id/4617).


### Acknowledgements


None.


### Get the Most Up to Date Product Security Information


To learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT), see the current list of NVIDIA security bulletins, or subscribe to security bulletin notifications, go to [NVIDIA Product Security](http://www.nvidia.com/product-security).


### Revision History


| Revision | Date | Description |
|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------|
| 3 | June 8, 2018 | Revised the availability of the updated version for BSP 21.7 |
| 2 | May 25, 2018 | Revised the availability of the updated version for BSP 24.2.3 and the expected availability of the updated version for BSP 21.7 |
| 1 | March 20, 2018 | Initial release |
##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA SHIELD TV Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4631/related/1)
* [ NVIDIA Shield TV and Tablet contain multiple vulnerabilities](/app/answers/detail/a_id/4548/related/1)
* [ NVIDIA Shield TV and Tablet contain multiple vulnerabilities](/app/answers/detail/a_id/4490/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [ NVIDIA Tegra Jetson L4T contains multiple vulnerabilities; updates for “BlueBorne” and “Dnsmasq”.](/app/answers/detail/a_id/4561/related/1)








