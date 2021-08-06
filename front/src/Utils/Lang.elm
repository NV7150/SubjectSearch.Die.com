module Utils.Lang exposing (..)


type Language
    = JA_JP
    | EN_US


type alias MultiLangText =
    { ja_jp: String
    , en_us: String
    }


mltext : Language -> MultiLangText -> String
mltext language text =
    case language of
        JA_JP ->
            text.ja_jp
        EN_US ->
            text.en_us
