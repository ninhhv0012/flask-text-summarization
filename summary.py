from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer_lstm = AutoTokenizer.from_pretrained('/model')
model_lstm = AutoModelForSeq2SeqLM.from_pretrained('/model',from_tf=True)

sentence = "Light Public Housing là một dự án xã hội quy mô lớn, chủ yếu phục vụ những người nộp đơn nằm trong danh sách chờ mua nhà xã hội từ 3 năm trở lên, ưu tiên cho người có gia đình. Hiện, nguồn cung không đủ nên trung bình người đăng ký mua nhà xã hội phải chờ gần 6 năm."
text = sentence + " </s>"
encoding = tokenizer_lstm(text, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cpu"), encoding["attention_mask"].to("cpu")
outputs = model_lstm.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    early_stopping=True
)
for output in outputs:
    line = tokenizer_lstm.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)