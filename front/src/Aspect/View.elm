module Aspect.View exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)

import Utils.Lang exposing (MultiLangText, mltext, Language)
import Model exposing (RootModel)
import Aspect.Model exposing (..)
import Html.Events exposing (onClick)
import Browser.Navigation as Nav

view : RootModel -> Html Msg
view model =
    div [ class "aspect-page" ]
        [ h1 []
            [ text
                <| mltext model.lang
                <| MultiLangText "アスペクト" "Aspect"
            ]
        , div [ class "classification"]
            <| List.map (classView model.lang) model.aspectPage.classList
        ]


classView : Language -> Classification -> Html Msg
classView lang c =
    div [ class "classification" ]
        [ h2 [] [ text <| mltext lang c.title ]
        , div [ class "aspects" ]
            <| List.map (aspectView lang) c.aspects
        ]


aspectView : Language -> Aspect -> Html Msg
aspectView lang aspect =
    a [ href ("/subjects?aspect=" ++ String.fromInt aspect.id) ] 
        [ div [ class "aspect" ]
            [ h3 []
                [ text <| mltext lang aspect.title ]
            , div [ class "subjects" ]
                [ text
                    <| String.join "　" 
                    <| List.map (mltext lang) aspect.subjectTitles
                ]
            ]
        ]
