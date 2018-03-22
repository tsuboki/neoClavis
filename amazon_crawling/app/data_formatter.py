class Data_formatter :
    def remove_comma_blank_jpysymbol_linechange(target_string) :
        return target_string.replace(',', "").replace(' ', "").replace('￥', "").replace('\n', "")

    def strip_and_remove_comma_linechange(target_string) :
        return target_string.strip().replace(',', "").replace('\n', "")

    def remove_review_comments_prefix_suffix(target_string):
        return target_string.replace('5つ星のうち',"").replace('件のカスタマーレビュー',"").replace(',', "").replace(' ', "").replace('￥', "").replace('\n', "")
