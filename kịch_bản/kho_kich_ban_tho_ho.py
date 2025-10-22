# file: kho_kich_ban_tho_ho.py

SCENARIOS_THO_HO = {
    "morning": [
        "Sáng sớm sương còn chưa tan chú đã phải dậy đi làm rồi, tranh thủ vào chào anh em một câu lấy may.",
        "Đêm qua chú đau lưng quá ngủ không ngon giấc, chỉ mong sáng nay vào nhóm có tin vui cho phấn chấn.",
        "Làm được một tay đầu ngày là có thêm tiền ăn cái bánh mì với ly cà phê cho tỉnh táo rồi.",
        "Công việc của chú làm ngoài trời nắng nôi vất vả nên có thêm đồng nào hay đồng đó các cháu ạ.",
        "Chú chuẩn bị trèo lên giàn giáo, ở trên đó không dùng điện thoại được nên có gì tối chú xem lại sau.",
        "Cả ngày người dính đầy xi măng, chỉ có lúc vào nhóm đọc tin nhắn của mọi người là chú thấy vui vẻ.",
        "Mỗi sáng thức dậy chú đều nghĩ đến việc phải cố gắng hơn để vợ con ở quê đỡ khổ.",
        "Hôm nay mà thắng được chút đỉnh thì chiều về chú sẽ mua thêm ít thịt cá để cải thiện bữa ăn.",
        "Chú vừa ăn vội gói xôi, chuẩn bị đi làm. Chúc cả nhà mình ở lại may mắn nhé.",
        "Tay chân chú lấm lem quen rồi, chỉ mong sao kiếm được đồng tiền sạch sẽ gửi về cho gia đình.",
        "Ở công trình ồn ào lắm, tiếng máy trộn bê tông át cả tiếng nói, nên chú chỉ xem chữ thôi.",
        "Chú tin tưởng các cháu có học thức, có sự tính toán, chắc chắn sẽ tốt hơn chú tự mày mò.",
        "Hôm qua đi làm về mệt quá chú ngủ quên mất, sáng nay vào thấy nhóm thắng lớn mà tiếc hùi hụi.",
        "Lại một ngày mới phải bán sức lao động, chỉ mong có ngày được về quê làm công việc nhẹ nhàng hơn.",
        "Thắng được một tay, coi như có tiền mua cho thằng cu ở nhà hộp sữa tốt hơn rồi.",
        "Chú đi làm đây, có kèo nào chắc ăn các cháu nhớ hú một tiếng nhé.",
        "Đôi bàn tay này của chú chai sạn hết cả rồi, chỉ mong đời con mình không vất vả như mình.",
        "Chú già rồi, không nhanh nhạy được như các cháu, nên cứ từ từ mà đi thôi.",
        "Mở mắt ra là thấy có tiền, cái cảm giác này nó vui khó tả lắm.",
        "Hy vọng hôm nay công việc suôn sẻ, nhóm mình cũng suôn sẻ luôn."
    ],
    "noon": [
        "Nghỉ trưa rồi, trời nắng gắt quá nên chú phải tìm vội một bóng râm ngồi tạm ăn hộp cơm.",
        "Vừa ăn xong hộp cơm bụi mà húp được một tay, tự nhiên thấy cơm ngon hơn hẳn.",
        "Thắng được một chút thôi mà quý lắm, nó bằng cả buổi chiều chú phơi nắng ngoài công trình rồi.",
        "Mồ hôi chảy ròng ròng ướt cả áo, may mà có tin vui từ nhóm làm chú thấy mát lòng mát dạ.",
        "Mấy anh em cùng làm cứ hỏi sao chú hay ngồi cười một mình, tại niềm vui này khó mà giải thích được.",
        "Chú xin phép chợp mắt một lát lấy sức, chiều còn phải trộn cả xe hồ nữa.",
        "Cảm ơn các cháu đã chỉ dẫn, chứ thân già như chú đâu biết gì về mấy cái này.",
        "Ăn vội vàng rồi lại phải ra làm ngay, hẹn gặp lại cả nhà mình vào lúc chiều tối nhé.",
        "Bữa cơm đạm bạc mà có thêm niềm vui từ nhóm thì không còn gì bằng.",
        "Chú đang ngồi dưới gốc cây, vừa phe phẩy cái nón vừa xem điện thoại.",
        "Tiền này chú sẽ để dành, cuối tháng gửi về cho vợ đóng tiền điện nước.",
        "Ở đây ai cũng tốt bụng, không chê chú già cả, chậm chạp. Chú biết ơn lắm.",
        "Thắng được một tay, có tiền mua chai nước ngọt uống cho lại sức rồi.",
        "Chú chỉ mong ngày nào cũng được đều đặn như này, không cần nhiều, chỉ cần an toàn.",
        "Nhìn các cháu trò chuyện rôm rả, chú cũng thấy mình như trẻ lại vài tuổi.",
        "Ăn xong rồi, chú phải phụ anh em một tay. Hẹn gặp lại cả nhà.",
        "Cái cảm giác sung sướng khi thắng nó giúp chú quên hết mệt mỏi.",
        "Chú sẽ không bao giờ quên sự giúp đỡ của mọi người đâu.",
        "Số tiền này tuy nhỏ nhưng nó giúp chú trang trải được nhiều thứ lắm.",
        "Lại có sức để chiến đấu với công việc buổi chiều rồi, cảm ơn nhóm mình."
    ],
    "evening": [
        "Chú vừa về đến phòng trọ, mệt rã rời nhưng việc đầu tiên vẫn là mở nhóm lên xem tình hình.",
        "Tắm rửa xong xuôi ngồi ăn cơm một mình, có nhóm trò chuyện chú cũng đỡ cảm thấy cô đơn.",
        "Cả ngày làm việc đã mệt, chú chỉ mong tối đến có thể kiếm thêm chút đỉnh để bù lại công sức.",
        "Hôm nay trên công trình có người bị tai nạn, nghĩ phận mình cũng mong manh nên phải cố gắng hơn.",
        "Số tiền lời hôm nay đủ để chú gửi về cho con bé nhà chú đóng tiền học thêm rồi, mừng rơi nước mắt.",
        "Chú không dám chơi lớn, cứ theo anh em một cách an toàn để tích tiểu thành đại thôi.",
        "Thôi chắc chú đi ngủ sớm để mai còn có sức đi làm, chúc các cháu ở lại gặp nhiều may mắn.",
        "Kết thúc một ngày vất vả mà có thêm thu nhập, bao nhiêu mệt nhọc của chú đều tan biến hết.",
        "Về tới phòng là chú phải xoa dầu vào mấy chỗ đau nhức, tuổi già không tha một ai.",
        "Chú vừa gọi điện về nhà, nghe giọng vợ con là lại có thêm động lực để cố gắng.",
        "Đêm đến nằm nghĩ lại thấy mình may mắn thật, gặp được đúng nơi để tin tưởng.",
        "Chú đang ngồi xem lại mấy cái phân tích của admin để học hỏi thêm, tuy chậm nhưng chú sẽ cố.",
        "Hôm nay chủ thầu trả lương, chú sẽ trích một phần để nạp thêm vốn, phải có đầu tư mới có thu hoạch.",
        "Ánh đèn phòng trọ hiu hắt, chỉ có ánh sáng từ điện thoại và sự sôi động của nhóm là làm chú vui.",
        "Chú chốt sổ ngày hôm nay, lãi được một khoản bằng mấy ngày công của chú rồi, không còn gì để chê.",
        "Cảm ơn các cháu đã luôn kiên nhẫn với một người già như chú.",
        "Chú đi ngủ đây, mai lại là một ngày dài. Chúc cả nhà ngủ ngon.",
        "Nằm trên giường mà vẫn không ngủ được vì vui quá, cứ nghĩ đến tương lai tốt đẹp hơn.",
        "Chú sẽ không bao giờ quên những ngày tháng khó khăn này và sự giúp đỡ của nhóm.",
        "Mỗi đồng tiền kiếm được đều là mồ hôi nước mắt, nên chú trân trọng lắm."
    ],
    "experience_motivation": [
        "Nói thật là từ ngày biết đến nhóm, cuộc sống của chú có thêm một niềm hy vọng lớn lắm.",
        "Trước đây chú làm quần quật quanh năm cũng chỉ đủ sống qua ngày, giờ thì đã dám mơ đến chuyện khác.",
        "Chú đang cố gắng tích cóp một số vốn để về quê mở tiệm tạp hóa nhỏ, không phải xa vợ xa con nữa.",
        "Mỗi lần nhận được tiền thắng, chú đều cảm thấy công sức mình bỏ ra được đền đáp xứng đáng.",
        "Chú khoe với các cháu, tháng này chú đã gửi được tiền về quê để sửa lại cái mái nhà bị dột.",
        "Ở đây chú không chỉ nhận được tiền mà còn nhận được sự quan tâm, chỉ bảo của mọi người, quý lắm.",
        "Ước mơ lớn nhất của đời chú là thấy vợ con được sống sung sướng hơn, và nhóm đang giúp chú thực hiện điều đó.",
        "Chú không biết dùng lời lẽ hoa mỹ, chỉ biết nói hai từ cảm ơn từ tận đáy lòng.",
        "Từ ngày có thêm thu nhập, chú ăn uống cũng thấy ngon miệng hơn, ngủ cũng sâu giấc hơn.",
        "Chú đã trả được hết mấy khoản nợ nhỏ vay mượn trước đây, cảm giác nhẹ cả người.",
        "Con chú nó khoe ở lớp được điểm cao, chú liền lấy tiền thắng để mua cho nó cái cặp sách mới.",
        "Chú biết thân phận mình thấp kém, nhưng ở đây chú được mọi người tôn trọng, chú rất cảm động.",
        "Mỗi lần rút được tiền về tài khoản, chú đều phải nhìn đi nhìn lại mấy lần mới tin là thật.",
        "Chú sẽ luôn ghi nhớ những lời khuyên của các cháu, không được tham lam, phải biết điểm dừng.",
        "Chú chỉ là một hạt cát nhỏ bé, nhưng nhờ có nhóm mà chú dám mơ đến việc xây cả một ngôi nhà.",
        "Chú hay kể về nhóm cho mấy anh em cùng làm, nhưng họ không tin. Thôi thì ai có duyên người ấy hưởng.",
        "Chú không mong giàu sang phú quý, chỉ mong cuộc sống ổn định, con cái được học hành đến nơi đến chốn.",
        "Nhờ có nhóm, chú mới biết đến chuyển tiền qua điện thoại, đúng là mở mang tầm mắt.",
        "Đây là thành quả của chú sau một tháng chắt bóp, chú đã mua được cho vợ cái điện thoại mới để gọi video cho dễ.",
        "Chú sẽ mãi là một thành viên trung thành của nhóm, dù sau này có khá hơn cũng không bao giờ quên."
    ],
    "interaction": [
        "Chú lớn tuổi rồi mắt hơi kém, cháu nào tốt bụng tóm tắt lại ý chính giúp chú với được không?",
        "Các cháu phân tích hay quá, chú nghe mà hiểu ra được nhiều điều.",
        "Chúc mừng cháu A nhé, nhìn các cháu thắng lớn chú cũng thấy vui lây.",
        "Tay này cầu khó đoán quá, thôi chú xin ngồi ngoài xem các cháu trổ tài cho an toàn.",
        "Chú có ít vốn còm thôi, các cháu bảo tay này chú nên vào bao nhiêu thì hợp lý?",
        "Lại thắng nữa rồi, đúng là đi theo mọi người là quyết định sáng suốt nhất của chú.",
        "Chú không rành mấy cái nút bấm, các cháu chỉ lại cho chú một lần nữa được không?",
        "Cảm ơn cháu B đã kiên nhẫn giải thích cho chú, chú hiểu rồi.",
        "Mạng ở công trình chập chờn lắm, có lúc chú không gửi được tin nhắn, các cháu thông cảm.",
        "Thấy các cháu đoàn kết giúp đỡ nhau, chú thấy ấm lòng lắm.",
        "Chú có sao nói vậy, có gì không phải các cháu bỏ qua cho người già này nhé.",
        "Tuyệt vời! Chú lại có tiền mua thuốc bổ cho bố mẹ ở quê rồi.",
        "Chú chỉ biết tin tưởng vào sự dẫn dắt của các cháu thôi.",
        "Kiến thức của chú có hạn, nên chỉ ngồi học hỏi là chính.",
        "Chú thấy cháu C nói rất có lý, tay này chú cũng nghĩ như vậy.",
        "Có cháu nào rành về cách nạp tiền không, chỉ giúp chú với.",
        "Chú vừa vào lệnh theo mọi người, giờ ngồi chờ tin vui thôi.",
        "Lại được ăn mừng rồi, cảm giác này thật tuyệt vời.",
        "Chú không biết nói gì hơn ngoài hai từ cảm ơn.",
        "Hy vọng nhóm mình sẽ ngày càng phát triển để giúp được nhiều người hơn nữa."
    ]
}

def expand_scenarios(scenarios, factor=4):
    expanded = {}
    for category, messages in scenarios.items():
        new_messages = list(messages)
        for _ in range(factor - 1):
            for msg in messages:
                variants = [f"{msg}, các cháu ạ.", f"Chú nói thật tình, {msg[0].lower()}{msg[1:]}", f"{msg}, mừng quá đi thôi!", f"Nghĩ lại thấy, {msg[0].lower()}{msg[1:]}"]
                new_messages.extend(variants)
        expanded[category] = list(set(new_messages))
    return expanded

SCENARIOS_THO_HO = expand_scenarios(SCENARIOS_THO_HO)