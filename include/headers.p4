/* -*- P4_16 -*- */
@controller_header("packet_in") header packet_in_header_t {
    egressSpec_t ingress_port;
    bit<7>     _pad;
}

@controller_header("packet_out") header packet_out_header_t {
    egressSpec_t egress_port;
    bit<7>     _pad;
}

header ethernet_t {
    bit<48>   dstAddr;
    bit<48>   srcAddr;
    bit<16>   etherType;
}

struct headers {
    ethernet_t   ethernet;
    packet_in_header_t  packet_in;
    packet_out_header_t packet_out;
}

struct mac_learn_digest_t {
    macAddr_t       srcAddr;
    egressSpec_t    ingress_port;
}

struct metadata {
    bool               send_mac_learn_msg;
    mac_learn_digest_t mac_learn_msg;
}