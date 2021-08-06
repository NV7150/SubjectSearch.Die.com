module Aspect.Model exposing (..)
import Utils.Lang exposing (MultiLangText)

type Msg
    = Msg1


type alias AspectModel =
    { classList : List Classification  -- (classification type, aspect list)
    }


type alias Classification =
    { title: MultiLangText
    , aspects: List Aspect
    }


type alias Aspect =
    { title: MultiLangText
    , subjectTitles : List MultiLangText
    }


-- FUNC
initModel : AspectModel
initModel =
    AspectModel []


fakeModel : AspectModel
fakeModel =
    -- 開発用
    { classList =
        [ Classification (MultiLangText "生きる方法論" "Life Methodology")
            <| List.repeat 12
                <| Aspect (MultiLangText "自然言語" "Natural Language")
                    <| List.repeat 20 (MultiLangText "言語と思考" "LANGUAGE AND THOUGHT")
        , Classification (MultiLangText "探求のスケール" "Scale of Inquiry")
            <| List.repeat 8
                <| Aspect (MultiLangText "ナノ" "Nano")
                    <| List.repeat 20 (MultiLangText "ゲノム分子生物学１" "GENOMIC MOLECULAR BIOLOGY 1")
        ]
    }
    

