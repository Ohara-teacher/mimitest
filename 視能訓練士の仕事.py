import streamlit as st

st.title("視能訓練士の仕事の問題")

# 質問と選択肢を定義
questions = {
    "医師の具体的指示を要するのはどれか。": {
        "options": ["調節検査", "視力検査", "色覚検査", "網膜電図検査", "両眼視機能検査"],
        "answer": "網膜電図検査"
    },
    "視能訓練士が行えないのはどれか。": {
        "options": ["視野検査", "眼位検査", "角膜形状解析", "涙液分泌機能検査", "涙道通水通色素検査"],
        "answer": "涙道通水通色素検査"
    },
    "視能訓練士法の規定で誤っているのはどれか。": {
        "options": ["視能訓練士とは厚生労働大臣の免許を受けた者である。", "視能訓練士と紛らわしい名称を使用してはならない。", "視能訓練士は両眼視機能の回復のために必要な検査を独自に行うことができる。", "業務上知り得た秘密は仕事を辞めても他人に漏らしてはいけない。", "免許を取り消された者の再免許取得の規定がある。"],
        "answer": "視能訓練士は両眼視機能の回復のために必要な検査を独自に行うことができる。"
    },
    "法令で視野検査ができないのはどれか": {
        "options": ["看護師", "助産師", "保健師", "臨床検査技師", "臨床研修中の医師"],
        "answer": "臨床検査技師"
    },
    "視能訓練士法について正しいのはどれか。": {
        "options": ["国家試験受験資格は独学で得られる。", "視能訓練は視能訓練士の業務独占である。", "免許を取り消されたら再免許は得られない。", "守秘義務は退職後５年間継続する。", "改姓した場合は30日以内に届出の義務がある。"],
        "answer": "改姓した場合は30日以内に届出の義務がある。"
    },
    "視能訓練士免許で誤っているのはどれか。": {
        "options": ["厚生労働大臣が交付する。", "試験合格者の申請により視能訓練士名簿に登録することで交付される。", "氏名を変更した者は30日以内に名簿の訂正を申請しなければならない。", "勤務先を変更したときは60日以内に名簿の訂正を申請しなければならない。", "本籍地に変更があったときは30日以内に名簿の訂正を申請しなければならない。"],
        "answer": "勤務先を変更したときは60日以内に名簿の訂正を申請しなければならない。"
   
    }
}

# セッションステートでページ番号の初期化
if 'page' not in st.session_state:
    st.session_state.page = 0

if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# 現在のページに表示する問題をスライスで取得
start_index = st.session_state.page * 5
end_index = start_index + 5
questions_page = list(questions.items())[start_index:end_index]

# 回答用の選択肢を作成
answers = {}
for q, data in questions_page:
    answers[q] = st.radio(q, data["options"])

# 結果表示ボタン
if st.button("結果を表示"):
    st.session_state.show_result = True

# 結果表示処理
if st.session_state.show_result:
    score = 0
    for q, data in questions_page:
        if answers[q] == data["answer"]:
            score += 1
            st.success(f"{q} ✅ 正解！")
        else:
            st.error(f"{q} ❌ 不正解！ 正解は「{data['answer']}」です。")
    st.write(f"あなたのスコア: {score}/{len(questions_page)}")

# 「前のページへ戻る」ボタンを表示
if st.session_state.page > 0:
    if st.button("前のページへ戻る"):
        st.session_state.page -= 1
        st.session_state.show_result = False  # 結果を消去してページを戻す



# 「次のページへ進む」ボタンを表示
if (st.session_state.page + 1) * 5 < len(questions):
    if st.button("次のページへ進む"):
        st.session_state.page += 1
        st.session_state.show_result = False  # 結果を消去してページを進める

