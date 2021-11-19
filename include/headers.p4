/* -*- P4_16 -*- */
// Ethernet 头部
header ethernet_t {
    bit<48>   dstAddr;
    bit<48>   srcAddr;
    bit<16>   etherType;
}

// 所有头部需要在此实例化
struct headers {
    ethernet_t   ethernet;
}

// 用户自定义的元数据结构体
struct metadata {
}