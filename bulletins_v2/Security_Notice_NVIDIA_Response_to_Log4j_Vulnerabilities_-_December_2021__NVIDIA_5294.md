

Security Notice: NVIDIA Response to Log4j Vulnerabilities - December 2021
=========================================================================




 Updated 02/14/2022 02:25 PM



This notice is a response to the remote code execution vulnerabilities in the Log4j Java library, which is also known as Log4Shell.






---




The CVE IDs of these vulnerabilities are as follows:


* [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
* [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046)
* [CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105)


 
NVIDIA is aware of these vulnerabilities and is evaluating their potential impact and relevance to its products and services. This page will be updated when any additional information becomes available regarding this issue.


### NVIDIA Products not Impacted


The following products have been analyzed by NVIDIA and are not vulnerable or impacted by this issue. NVIDIA is continuing its investigations and will update this list as new information becomes available. NVIDIA’s products or services that are not listed below are undergoing investigation.


* GeForce Experience client software
* GeForceNOW client software
* GPU Display Drivers for Windows and Linux
* L4T Jetson Products
* NVIDIA Broadcast
* NVIDIA Maxine
* SHIELD TV
* All Networking products (except for [NetQ](#netq), which is one of the remediated NVIDIA products)


### Remediated NVIDIA Products


The following sections list the NVIDIA products affected, versions affected, and the updated versions available or mitigations that require customer action.


* [CUDA Toolkit Visual Profiler and Nsight Eclipse Edition](#cuda-vprof-and-nsight-eclipse)
* [DGX Systems](#dgx-systems)
* [NetQ](#netq)
* [vGPU Software License Server](#vgpu-software-license-server)


#### CUDA Toolkit Visual Profiler and Nsight Eclipse Edition


| CVE IDs Addressed | Product Name | Affected Versions | Updated Version | Mitigation for Affected Versions |
|:-----------------------------------------------|:------------------------------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CVE‑2021‑44228 CVE‑2021‑45046 CVE‑2021‑41505 | CUDA Toolkit Visual Profiler | Visual Profiler in CUDA Toolkit version 11.5 and prior versions | CUDA Toolkit version 11.6.0 CUDA Toolkit updates 11.5.2 and 11.4.4 will be available in February 2022. | Log4j is included in CUDA Toolkit. However it is not being used and there is no risk to users who have the Log4j files. Because they are not being used, an update is being prepared to remove the Log4j files[1] from CUDA Toolkit. If concerned, customers can safely delete the files as a mitigation. |
| CVE‑2021‑44228 CVE‑2021‑45046 CVE‑2021‑41505 | CUDA Toolkit Nsight Eclipse Edition | Nsight Eclipse Edition in CUDA Toolkit prior to version 11.0 | Nsight Eclipse Plugins Edition in CUDA Toolkit version 11.0 or later Updates for version 10.2 will be available in February 2022. | Update to an Nsight Eclipse Plugins Edition in CUDA Toolkit version 11.0 or later Alternatively, note that Log4j is included in CUDA Toolkit 10.2 and earlier. However it is not being used and there is no risk to users who have the Log4j files. Because they are not being used, an update is being prepared to remove the Log4j files[2] from CUDA Toolkit 10.2 updates. If concerned, customers can safely delete the files as a mitigation. |
[1] For example: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\libnvvp\plugins\org.apache.ant_1.9.2.v201404171502\lib\ant-apache-log4j.jar`


[2] For example: `/usr/local/cuda/libnsight/plugins/org.apache.ant_1.9.2.v201404171502/lib/ant-apache-log4j.jar`


#### DGX Systems


By default, DGX systems are not exposed to this issue. NVIDIA did not include the Log4j Java library in its DGX OS releases, but this library might have been installed by a user as additional software. To check if a version of the `liblog4j2-java` library built from a vulnerable `apache-log4j2` source package is installed on your system, run the following command:



```

$ **apt-cache policy liblog4j2-java**
liblog4j2-java:
  Installed: (none)
  Candidate: 2.10.0-2ubuntu0.1
```

Fixes to address this issue are available from Canonical in the updated versions listed in the following table.


If a version of the `liblog4j2-java` library built from a vulnerable `apache-log4j2` source package is installed, run the following commands to get the updated version:



```

$ **sudo apt update**
$ **sudo apt full-upgrade**
```

| CVE IDs Addressed | Product Name | Affected Product or Component Version | Updated Product or Component Version |
|:--------------------|:------------------------------------------------------|:-----------------------------------------------------|:-----------------------------------------------|
| CVE‑2021‑44228 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 5: liblog4j2-java 2.14.1 and prior versions | DGX OS 5: liblog4j2-java 2.16.0-0.20.04.1 |
| CVE‑2021‑44228 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 4: liblog4j2-java 2.10.0-2 and prior versions | DGX OS 4: liblog4j2-java 2.10.0-2ubuntu0.1 |
| CVE‑2021‑45046 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 5: liblog4j2-java 2.14.1 and prior versions | DGX OS 5: liblog4j2-java 2.17.0-0.20.04.1 |
| CVE‑2021‑45046 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 4: Not impacted | DGX OS 4: Not impacted |
| CVE‑2021‑45105 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 5: liblog4j2-java 2.14.1 and prior versions | DGX OS 5: liblog4j2-java 2.17.0-0.20.04.1 |
| CVE‑2021‑45105 | DGX-1, DGX-2, DGX A100, DGX Station, DGX Station A100 | DGX OS 4: liblog4j2-java 2.10.0-2 and prior versions | DGX OS 4: Remediation expected January 2022. |
For more information about this issue, refer to the [Log4Shell](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/Log4Shell) page on the Ubuntu wiki.


#### NetQ


| CVE IDs Addressed | Product Name | Affected Version | Updated Version |
|:-----------------------------------------------|:---------------|:-----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CVE‑2021‑44228 CVE‑2021‑45046 CVE‑2021‑45105 | NetQ | Versions 2.x, 3.x, and 4.0.x | SaaS instances are patched. Upgrade on-premises telemetry servers to the 4.1.0 release by following NetQ Upgrade Guide. If you are a SaaS customer, you should also upgrade OPTA servers to 4.1.0. |
#### vGPU Software License Server


| CVE IDs Addressed | Product Name | Affected Product or Component Version | Mitigation |
|:-----------------------------------------------|:-----------------------------|:----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CVE‑2021‑44228 CVE‑2021‑45046 CVE‑2021‑45105 | vGPU software license server | 2021.07 and 2020.05 Update 1 | Apply the mitigation described in Log4j Java Vulnerability (CVE-2021-44228 and CVE-2021-45046) for Legacy vGPU Software License Server in the NVIDIA knowledge base. |
### Get the Most Up to Date Product Security Information


To learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT), see the current list of NVIDIA security bulletins, or subscribe to security bulletin notifications, go to [NVIDIA Product Security](https://www.nvidia.com/en-us/security/).


### Revision History


| Revision | Date | Description |
|-----------:|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 9 | February 2, 2022 | Added information about CUDA Toolkit updates |
| 8 | January 4, 2022 | Added NVIDIA Maxine and Broadcast products to the list of products that are not impacted. Added information about CVE‑2021‑45105 for vGPU software license server |
| 7 | December 22, 2021 | Added GPU display driver for Linux and networking products to the list of products that are not impacted. |
| 6 | December 21, 2021 | Added GPU Display Driver for Windows to the list of products that are not impacted. Added information about CVE‑2021‑45105 for DGX OS. |
| 5 | December 20, 2021 | Added a section for unaffected product list and included CVE‑2021‑45105 in this response. Added remediation update information about CVE-2021-45105 for NETQ. |
| 4 | December 17, 2021 | Added update information for CUDA Toolkit and included CVE‑2021‑45046 in this response. |
| 3 | December 16, 2021 | Added update information for NetQ. |
| 2 | December 15, 2021 | Added update information for DGX OS Software and mitigation information for the vGPU software license server. |
| 1 | December 13, 2021 | Initial release. |
### Support


If you have any questions about this security notice, contact [NVIDIA Support](https://www.nvidia.com/en-us/support/).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GPU Display Driver - October 2021](/app/answers/detail/a_id/5230/related/1)
* [Security Notice: NVIDIA GPU and Tegra Hardware - November 2021](/app/answers/detail/a_id/5263/related/1)
* [Where can I get CUDA Toolkit?](/app/answers/detail/a_id/3161/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)
* [ NVIDIA GeForce Experience - February 2021](/app/answers/detail/a_id/5155/related/1)








