//PART1
1. What are the most popular hypervisors for infrastructure virtualization?
Type1: Microsoft Hyper-V. VMware ESX Server. Citrix XenServer
Type2: VMware Workstation, Oracle VM VirtualBox, Microsoft Virtual PC, Parallels Desktop
Type3: VMware ESX, Microsoft Hyper-V, KVM

2. Briefly describe the main differences of the most popular hypervisors.
A Type 1 hypervisor runs directly on the host machine's physical hardware, and it's referred to as a bare-metal hypervisor. The Type 1 hypervisor doesn't have to load an underlying OS.
Microsoft Hyper-V. Microsoft Hyper-V runs on Windows OSes and enables admins to run multiple OSes inside a VM. Admins and developers often use Hyper-V to build test environments to run software on several OSes by creating VMs for each test.
VMware vSphere. VMware vSphere includes the ESXi hypervisor and vCenter management software to provide a suite of virtualization products, such as the vSphere Client, vSphere software development kits, Storage vMotion, the Distributed Resource Scheduler and Fault Tolerance. VMware vSphere is geared toward enterprise data centers; smaller businesses might find it difficult to justify the price.
KVM. The KVM hypervisor is an open source virtualization architecture made for Linux distributions. 

A Type 2 hypervisor is typically installed on top of an existing OS. It is sometimes called a hosted hypervisor. Type 2 hypervisors are generally not used for data center computing and are reserved for client or end-user systems.
Oracle VM VirtualBox. Oracle VM VirtualBox is an open source hosted hypervisor that runs on a host OS to support guest VMs. VirtualBox supports a variety of host OSes, such as Windows, Apple macOS, Linux and Oracle Solaris.
VMware Workstation Pro and VMware Fusion. VMware Workstation Pro is a 64-bit hosted hypervisor capable of implementing virtualization on Windows and Linux systems. Some of Workstation's features include host/guest file sharing, the creation and deployment of encrypted VMs, and VM snapshots.
QEMU. QEMU is an open source virtualization tool that emulates CPU architectures and enables developers and admins to run applications compiled for one architecture on another. QEMU offers features such as support for non-volatile dual in-line memory module hardware, share file system, secure guests and memory encryption.

A Type 3 hypervisor  is the monolithic hypervisor, which includes hardware device drivers (hardware virtualization).Microkernel. In this case, device drivers are located inside the host operating system. In this case, the host operating system, like guest, runs in a virtual environment and is called the "parent". Only the parent operating system has access to the hardware, the daughter ones, in turn, can interact with the hardware only through the "parent".
VMware ESX a robust, bare-metal hypervisor that installs directly onto the physical server. With direct access to and control of underlying resources, VMware ESXi effectively partitions hardware to consolidate applications and cut costs. It’s the industry leader for efficient architecture, setting the standard for reliability, performance, and support. 
Microsoft Hyper-V implements isolation of virtual machines in terms of a partition. A partition is a logical unit of isolation, supported by the hypervisor, in which each guest operating system executes. There must be at least one parent partition in a hypervisor instance, running a supported version of Windows Server (2008 and later). The virtualization software runs in the parent partition and has direct access to the hardware devices. 

//PART2
1. Install Oracle VM Virtual Box 6.1.28
2. Activate hardware virtualisation
3. Create virtual machine VM1 with OS Manjaro-xfce-21.1.6 (64bit)
4. Clone virtual machine
5. Add USB
6. Add dir
7. Check network settings: 
NAT (local IP 10.0.2.15) - NAT inside VM by VirtualBox ::				VM1 ping VM2 - false, 	VM ping  Host - false
Bridge adapter (get IP from Mikrotik DHCP server IP 192.168.88.X/24) ::			VM1 ping  VM2 -true, 	VM ping  Host - true
Host-only adapter - get IP from VirtualBox(VM1 & VM2 in one LAN 192.168.56.X/24) :: 	VM1 ping  VM2 -true, 	VM ping  Host - false

8. Work with VBoxManage is shoven in screenshots 

9. Install Vagrant 2.2.19
10. 