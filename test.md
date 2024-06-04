Security Bulletin: Triton Inference Server - May 2024

**Answer ID: 5546**

NVIDIA has released a software update for NVIDIA Triton Inference Server to address the issues disclosed in this bulletin. To protect your system, install the latest release from the [<span class="underline">Triton Inference Server Releases</span>](https://github.com/triton-inference-server/server/releases) page on GitHub, and view the [<span class="underline">Secure Deployment Considerations Guide</span>](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md).

Go to [<span class="underline">NVIDIA Product Security</span>](https://www.nvidia.com/security/).

### Details

This section provides a summary of the potential vulnerabilities that this security update addresses and their impact. The descriptions use [<span class="underline">CWE™</span>](https://cwe.mitre.org/), and base scores and vectors use [<span class="underline">CVSS v3.1</span>](https://www.first.org/cvss/v3.1/user-guide) standards.

<table>
<tbody>
<tr class="odd">
<td><strong>CVE ID</strong></td>
<td><strong>Description</strong></td>
<td><strong>Vector</strong></td>
<td><strong>Base Score</strong></td>
<td><strong>Severity</strong></td>
<td><strong>CWE</strong></td>
<td><strong>Impacts</strong></td>
</tr>
<tr class="even">
<td><p>CVE-2024-0103</p>
<p><a href="https://nvbugspro.nvidia.com/bug/4607386"><span class="underline">4607386</span></a></p>
<p>(dupe: 4629688)</p></td>
<td>NVIDIA Triton Inference Server for Linux and Windows contains a vulnerability where a user may cause an incorrect initialization of a resource by network issue. A successful exploit of this vulnerability may lead to information disclosure.</td>
<td><a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N&amp;version=3.1"><span class="underline">AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N</span></a></td>
<td>5.4</td>
<td>Medium</td>
<td><a href="https://cwe.mitre.org/data/definitions/1419.html"><span class="underline">CWE-1419</span></a></td>
<td>Information disclosure</td>
</tr>
<tr class="odd">
<td><p>CVE-2024-0095</p>
<p><a href="https://nvbugspro.nvidia.com/bug/4492806"><span class="underline">4492806</span></a></p></td>
<td>NVIDIA Triton Inference Server for Linux and Windows contains a vulnerability where a user can inject forged logs and executable commands by injecting arbitrary data as a new log entry. A successful exploit of this vulnerability might lead to data tampering.</td>
<td><a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N&amp;version=3.1"><span class="underline">AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N</span></a></td>
<td>4.3</td>
<td>Medium</td>
<td><a href="https://cwe.mitre.org/data/definitions/117.html"><span class="underline">CWE-117</span></a></td>
<td>Data tampering</td>
</tr>
</tbody>
</table>

The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.

### Security Updates

The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.

<table>
<tbody>
<tr class="odd">
<td><strong>CVE IDs Addressed</strong></td>
<td><strong>Affected Products</strong></td>
<td><strong>Platform or OS</strong></td>
<td><strong>Affected Versions</strong></td>
<td><strong>Updated Version</strong></td>
</tr>
<tr class="even">
<td><p>CVE-2024-0095</p>
<p><a href="https://nvbugspro.nvidia.com/bug/4492806"><span class="underline">4492806</span></a></p></td>
<td>NVIDIA Triton Inference Server</td>
<td>Linux, Windows</td>
<td>20.10 to 24.04</td>
<td>24.05</td>
</tr>
<tr class="odd">
<td><p>CVE-2024-0103</p>
<p><a href="https://nvbugspro.nvidia.com/bug/4607386"><span class="underline">4607386</span></a></p></td>
<td>NVIDIA Triton Inference Server</td>
<td>Linux, Windows</td>
<td>23.10 to 24.04</td>
<td>24.05</td>
</tr>
</tbody>
</table>

### 

#### Notes

  - Users deploying NVIDIA Triton Inference Server in production settings should follow the [<span class="underline">Secure Deployment Considerations Guide</span>](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md) and ensure that logging and shared memory APIs are protected for use by authorized users.

### Acknowledgements

NVIDIA thanks the following individuals for reporting these issues:

CVE-2024-0095: pinkdraconian

CVE-2024-0103: Andrew Innes, Will Williams, Jamie Dougherty, Markus Hennerbichler

### Get the Most Up-to-Date Product Security Information

Visit the [<span class="underline">NVIDIA Product Security</span>](https://www.nvidia.com/security) page to

  - Subscribe to security bulletin notifications

  - See the current list of NVIDIA security bulletins

  - Report a potential security issue in any NVIDIA supported product

  - Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)

### Revision History

|              |              |                 |
| ------------ | ------------ | --------------- |
| **Revision** | **Date**     | **Description** |
| 1.0          | May 24, 2024 | Initial release |

### Support

If you have any questions about this security bulletin, contact [<span class="underline">NVIDIA Support</span>](https://www.nvidia.com/object/support.html).

##### **Disclaimer**

ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.

Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.
