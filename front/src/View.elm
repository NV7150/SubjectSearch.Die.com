module View exposing (..)
import Url.Parser
import Browser

import Model exposing (RootModel, Msg(..), Route(..))
import Html exposing (..)
import Html.Attributes exposing (..)
import Utils.Lang exposing (MultiLangText, mltext, Language)
import Aspect.View



view : RootModel -> Browser.Document Msg
view model =
    let 
        doc =
            case Url.Parser.parse Model.routeParser model.url of
                Just (Home, _) ->
                    { title = mltext model.lang <| MultiLangText "ホーム" "Home"
                    , body =
                        div [ class "indexpage" ]
                            [ a [ href "/aspect" ] [ text "/aspect" ] 
                            , a [ href "/en/aspect" ] [ text "/en/aspect"]
                            ]
                    }
                Just (AspectIndex, _) ->
                    { title = mltext model.lang <| MultiLangText "ジャンル別" "By Genre"
                    , body =
                        Aspect.View.view model
                            |> Html.map AspectMsg
                    }
                Nothing ->
                    { title = "404"
                    , body =
                        div []
                            [ text "404 not found" ]
                    }
    in
        { title = doc.title ++ (mltext model.lang <| MultiLangText " | 科目検索.死ぬ.com" " | SubjectSearch.Die.com")
        , body =
            [ navView model
            , div[ id "app" ]
                [ doc.body ]
            , footerView model
            ]
        }


navView : RootModel -> Html Msg
navView model =
    nav [ id "nav" ]
        [ div [ id "logo" ]
            [ a [ href "/" ]
                [ p [] 
                    [ text
                        <| mltext model.lang <| MultiLangText "科目検索.死ぬ.com" "SubjectSearch.Die.com"
                    ]
                ]
            ]
        , div [ id "searchbox", class "searchbox" ]
            [ 
            ]
        ]


footerView : RootModel -> Html msg
footerView model =
    footer [ id "footer" ]
        [ footerAbout model.lang
        , footerSitemap model.lang
        , footerContribute model.lang
        ]


footerAbout : Language -> Html msg
footerAbout lang =
    div [ class "about" ]
            [ h1 []
                [ span [ class "logo"]
                    [ text 
                        <| mltext lang <| MultiLangText "科目検索.死ぬ.com" "SubjectSearch.Die.com"
                    ]
                ]
            , p []
                [ text 
                    <| mltext lang
                    <| MultiLangText
                        "SFCの履修登録をサポートするWEBサイトです."
                        "This is a website to support SFC course registration."
                ]
            , h2 []
                [ text 
                    <| mltext lang
                    <| MultiLangText "クレジット" "Credit"
                ]
            , div [ class "credit" ]
                [ p []
                    [ a [ href "https://github.com/kekeho" ]
                        [ text "kekeho" ]
                    ]
                , p []
                    [ a [ href "https://github.com/NV7150"] 
                        [ text "dango" ]
                    ]
                , p []
                    [ a [ href ""] 
                        [ text "Nanastasia" ]
                    ]
                , p []
                    [ a [ href ""] 
                        [ text "Sukaneki" ]
                    ]
                ]
            ]


footerSitemap : Language -> Html msg
footerSitemap lang =
    div [ class "sitemap" ]
            [ h1 [ class "sitemap" ] 
                [ text 
                    <| mltext lang
                    <| MultiLangText
                        "サイトマップ" 
                        "Sitemap"
                ]
            ]


footerContribute : Language -> Html msg
footerContribute lang =
    div [ class "contribute" ]
        [ h1 [ class "contribute" ]
            [ text
                <| mltext lang
                <| MultiLangText
                    "コントリビュート!"
                    "Contribute!"
            ]
        , p []
            [ text
                <| mltext lang
                <| MultiLangText
                    """このサービスは, 有志によって開発・運営されています.
                    いくつかの方法で, 貢献することができます! 私達をサポートしてください."""
                    """This service is developed and operated by volunteers.
                    You can contribute in several ways! Please support us."""
            ]
        , div [ class "github" ]
            [ h2 [] [ text "GitHub" ]
            , p []
                [ a [ href "https://github.com/NV7150/SubjectSearch.Die.com"] 
                    [ text "NV7150/SubjectSearch.Die.com" ]
                ]
            , p [] 
                [ text
                    <| mltext lang
                    <| MultiLangText
                        "GitHubにて, バグの報告・修正などに協力していただけると助かります."
                        "We would appreciate it if you could help us by reporting and fixing bugs on GitHub."
                ]
            ]
        , div [ class "coin" ]
            [ h2 [] [ text "Ethereum" ]
            , p []
                [ text 
                    <| mltext lang
                    <| MultiLangText
                        "サーバー運営には, とてもお金がかかります. 安定した運営を続けていくために, 仮想通貨で私達をサポートしてください."
                        "It costs a lot of money to run a server. In order to keep the server stable, please support us with crypto currency."
                ]
            , p [ class "eth-address" ]
                [ text "0x6D2b73dd844c55627801755D69DB151ae80C03af" ]
            , p [ class "etherscan" ]
                [ a [ href "https://etherscan.io/address/0x6d2b73dd844c55627801755d69db151ae80c03af" ] 
                    [ text 
                        <| mltext lang
                        <| MultiLangText
                            "集まった金額をetherscan.ioで見る"
                            "View the amount collected at etherscan.io"
                    ]
                ] 
            ]
        ]
