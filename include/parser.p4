parser ParserImpl(packet_in packet,
                  out headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
    // p4 从 start 开始解析报文
    state start {
        // 转到 parse_ethernet 状态
        transition parse_ethernet;
    }

    // 解析 Ethernet 报头
    state parse_ethernet {
        packet.extract(hdr.ethernet);
        // accept 结束解析头部
        transition accept;
    }
}

control DeparserImpl(packet_out packet, in headers hdr) {
    apply {
        // 重新封装报文头部
        packet.emit(hdr.ethernet);
    }
}