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

    // 动作：丢弃报文
    action drop() {
        mark_to_drop(standard_metadata);
    }
    // 动作：广播报文
    action multicast() {
        standard_metadata.mcast_grp = 1;
    }
    // 动作：转发到特定端口
    // port：出端口
    action mac_forward(egressSpec_t port) {
        standard_metadata.egress_spec = port;
    }
    // mac 地址表，用于二层数据报文转发
    table mac_lookup {
        key = {
            // 根据 mac 目的地址匹配
            hdr.ethernet.dstAddr: exact;
        }
        // 该表支持的所有动作，与上面 action 对应
        actions = {
            mac_forward;
            multicast;
            drop;
        }
        // 该表大小
        size = 128;
        // 默认匹配不到就丢弃报文
        default_action = drop();
    }

    apply {
        // 如果是 Ethernet 报文就执行地址表转发
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
        // 如果出端口与入端口是相同的，则丢弃报文
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
