/* -*- P4_16 -*- */
// #define V1MODEL_VERSION 20200408
#include <core.p4>
#include <v1model.p4>
#include "include/define.p4"
#include "include/headers.p4"
#include "include/checksum.p4"
#include "include/parser.p4"


control IngressImpl(inout headers hdr,
                    inout metadata meta,
                    inout standard_metadata_t standard_metadata) {

    action drop() {
        mark_to_drop(standard_metadata);
    }

    action multicast() {
        standard_metadata.mcast_grp = 1;
    }

    action mac_forward(egressSpec_t port) {
        standard_metadata.egress_spec = port;
    }

    table mac_lookup {
        key = {
            hdr.ethernet.dstAddr: exact;
        }
        actions = {
            mac_forward;
            multicast;
            drop;
        }
        size = 128;
        default_action = drop();
    }

    apply {
        if (hdr.ethernet.isValid())
            mac_lookup.apply();
    }
}

control EgressImpl(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {

    action drop() {
        mark_to_drop(standard_metadata);
    }

    apply {
        if (standard_metadata.egress_port == standard_metadata.ingress_port)
            drop();
    }
}

V1Switch(
    ParserImpl(),
    VerifyChecksumImpl(),
    IngressImpl(),
    EgressImpl(),
    ComputeChecksumImpl(),
    DeparserImpl()
) main;
