---
id: "lfs-design-conclusion"
type: "concept"
domain: "project"
title: "DESIGN: Conclusion"
summary: "And that's littlefs, thanks for reading!"
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#conclusion"
license: "BSD-3-Clause"
mode: "V"
---

And that's littlefs, thanks for reading!


[wikipedia-flash]: https://en.wikipedia.org/wiki/Flash_memory
[wikipedia-sna]: https://en.wikipedia.org/wiki/Serial_number_arithmetic
[wikipedia-crc]: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
[wikipedia-cow]: https://en.wikipedia.org/wiki/Copy-on-write
[wikipedia-B-tree]: https://en.wikipedia.org/wiki/B-tree
[wikipedia-B+-tree]: https://en.wikipedia.org/wiki/B%2B_tree
[wikipedia-skip-list]: https://en.wikipedia.org/wiki/Skip_list
[wikipedia-ctz]: https://en.wikipedia.org/wiki/Count_trailing_zeros
[wikipedia-ecc]: https://en.wikipedia.org/wiki/Error_correction_code
[wikipedia-hamming-bound]: https://en.wikipedia.org/wiki/Hamming_bound
[wikipedia-dynamic-wear-leveling]: https://en.wikipedia.org/wiki/Wear_leveling#Dynamic_wear_leveling
[wikipedia-static-wear-leveling]: https://en.wikipedia.org/wiki/Wear_leveling#Static_wear_leveling
[wikipedia-ftl]: https://en.wikipedia.org/wiki/Flash_translation_layer

[oeis]: https://oeis.org
[A001511]: https://oeis.org/A001511
[A005187]: https://oeis.org/A005187

[fat]: https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system
[ext2]: http://e2fsprogs.sourceforge.net/ext2intro.html
[jffs]: https://www.sourceware.org/jffs2/jffs2-html
[yaffs]: https://yaffs.net/documents/how-yaffs-works
[spiffs]: https://github.com/pellepl/spiffs/blob/master/docs/TECH_SPEC
[ext4]: https://ext4.wiki.kernel.org/index.php/Ext4_Design
[ntfs]: https://en.wikipedia.org/wiki/NTFS
[btrfs]: https://btrfs.wiki.kernel.org/index.php/Btrfs_design
[zfs]: https://en.wikipedia.org/wiki/ZFS

[cow]: https://upload.wikimedia.org/wikipedia/commons/0/0c/Cow_female_black_white.jpg
[elephant]: https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg
[ram]: https://upload.wikimedia.org/wikipedia/commons/9/97/New_Mexico_Bighorn_Sheep.JPG

[metadata-formula1]: https://latex.codecogs.com/svg.latex?cost%20%3D%20n%20+%20n%20%5Cfrac%7Bs%7D%7Bd+1%7D
[metadata-formula2]: https://latex.codecogs.com/svg.latex?s%20%3D%20r%20%5Cfrac%7Bsize%7D%7Bn%7D
[metadata-formula3]: https://latex.codecogs.com/svg.latex?d%20%3D%20%281-r%29%20%5Cfrac%7Bsize%7D%7Bn%7D
[metadata-formula4]: https://latex.codecogs.com/svg.latex?cost%20%3D%20n%20+%20n%20%5Cfrac%7Br%5Cfrac%7Bsize%7D%7Bn%7D%7D%7B%281-r%29%5Cfrac%7Bsize%7D%7Bn%7D+1%7D

[ctz-formula1]: https://latex.codecogs.com/svg.latex?%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%5Cleft%28%5Ctext%7Bctz%7D%28i%29+1%5Cright%29%20%3D%20%5Csum_%7Bi%3D0%7D%5Cfrac%7B1%7D%7B2%5Ei%7D%20%3D%202
[ctz-formula2]: https://latex.codecogs.com/svg.latex?B%20%3D%20%5Cfrac%7Bw%7D%7B8%7D%5Cleft%5Clceil%5Clog_2%5Cleft%28%5Cfrac%7B2%5Ew%7D%7BB-2%5Cfrac%7Bw%7D%7B8%7D%7D%5Cright%29%5Cright%5Crceil
[ctz-formula3]: https://latex.codecogs.com/svg.latex?N%20%3D%20%5Csum_i%5En%5Cleft%5BB-%5Cfrac%7Bw%7D%7B8%7D%5Cleft%28%5Ctext%7Bctz%7D%28i%29+1%5Cright%29%5Cright%5D
[ctz-formula4]: https://latex.codecogs.com/svg.latex?%5Csum_i%5En%5Cleft%28%5Ctext%7Bctz%7D%28i%29+1%5Cright%29%20%3D%202n-%5Ctext%7Bpopcount%7D%28n%29
[ctz-formula5]: https://latex.codecogs.com/svg.latex?N%20%3D%20Bn%20-%20%5Cfrac%7Bw%7D%7B8%7D%5Cleft%282n-%5Ctext%7Bpopcount%7D%28n%29%5Cright%29
[ctz-formula6]: https://latex.codecogs.com/svg.latex?n%20%3D%20%5Cleft%5Clfloor%5Cfrac%7BN-%5Cfrac%7Bw%7D%7B8%7D%5Cleft%28%5Ctext%7Bpopcount%7D%5Cleft%28%5Cfrac%7BN%7D%7BB-2%5Cfrac%7Bw%7D%7B8%7D%7D-1%5Cright%29+2%5Cright%29%7D%7BB-2%5Cfrac%7Bw%7D%7B8%7D%7D%5Cright%5Crfloor
[ctz-formula7]: https://latex.codecogs.com/svg.latex?%5Cmathit%7Boff%7D%20%3D%20N%20-%20%5Cleft%28B-2%5Cfrac%7Bw%7D%7B8%7D%5Cright%29n%20-%20%5Cfrac%7Bw%7D%7B8%7D%5Ctext%7Bpopcount%7D%28n%29

[bigB]: https://latex.codecogs.com/svg.latex?B
[d]: https://latex.codecogs.com/svg.latex?d
[m]: https://latex.codecogs.com/svg.latex?m
[bigN]: https://latex.codecogs.com/svg.latex?N
[n]: https://latex.codecogs.com/svg.latex?n
[n']: https://latex.codecogs.com/svg.latex?n%27
[r]: https://latex.codecogs.com/svg.latex?r
[s]: https://latex.codecogs.com/svg.latex?s
[w]: https://latex.codecogs.com/svg.latex?w
[x]: https://latex.codecogs.com/svg.latex?x

[metadata-cost-graph]: https://raw.githubusercontent.com/geky/littlefs/gh-images/metadata-cost.svg?sanitize=true
[wear-distribution-graph]: https://raw.githubusercontent.com/geky/littlefs/gh-images/wear-distribution.svg?sanitize=true
[file-cost-graph]: https://raw.githubusercontent.com/geky/littlefs/gh-images/file-cost.svg?sanitize=true
