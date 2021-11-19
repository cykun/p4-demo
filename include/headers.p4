/* -*- P4_16 -*- */
header ethernet_t {
    bit<48>   dstAddr;
    bit<48>   srcAddr;
    bit<16>   etherType;
}

struct headers {
    ethernet_t   ethernet;
}

struct metadata {
}